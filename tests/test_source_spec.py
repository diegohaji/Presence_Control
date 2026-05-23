from __future__ import annotations

from pathlib import Path

import pytest

from presence_control import cli
from presence_control.source_selector import SourceSelectionCancelled, probe_webcams, select_source
from presence_control.video_source import SourceSpec, VideoSourceError, open_capture, parse_source_spec


class FakeCapture:
    def __init__(self, opened: bool):
        self.opened = opened
        self.released = False

    def isOpened(self) -> bool:
        return self.opened

    def release(self) -> None:
        self.released = True


class FakeCv2:
    def __init__(self, opened_by_arg):
        self.opened_by_arg = opened_by_arg
        self.captures = []

    def VideoCapture(self, arg):
        capture = FakeCapture(self.opened_by_arg.get(arg, False))
        self.captures.append((arg, capture))
        return capture


def test_parse_webcam_source_spec():
    spec = parse_source_spec("webcam:0")

    assert spec.kind == "webcam"
    assert spec.value == 0


def test_parse_file_source_spec():
    spec = parse_source_spec("videos/test.mp4")

    assert spec.kind == "file"
    assert spec.value == Path("videos/test.mp4")


def test_empty_source_raises_actionable_error():
    with pytest.raises(VideoSourceError, match="webcam.*video file"):
        parse_source_spec("")


def test_failed_open_raises_with_retry_guidance(monkeypatch):
    fake_cv2 = FakeCv2({0: False})
    monkeypatch.setattr("presence_control.video_source.cv2", fake_cv2)

    with pytest.raises(VideoSourceError, match="Try another camera index"):
        open_capture(SourceSpec(kind="webcam", value=0, raw="webcam:0"))

    assert fake_cv2.captures[0][1].released is True


def test_open_capture_uses_file_path(monkeypatch):
    video_path = Path("videos/test.mp4")
    fake_cv2 = FakeCv2({str(video_path): True})
    monkeypatch.setattr("presence_control.video_source.cv2", fake_cv2)

    capture = open_capture(SourceSpec(kind="file", value=video_path, raw="videos/test.mp4"))

    assert capture.isOpened()
    assert fake_cv2.captures[0][0] == str(video_path)


def test_webcam_probe_releases_every_capture(monkeypatch):
    fake_cv2 = FakeCv2({0: True, 1: False, 2: True})
    monkeypatch.setattr("presence_control.source_selector.cv2", fake_cv2)

    assert probe_webcams(max_index=3) == [0, 2]
    assert [capture.released for _, capture in fake_cv2.captures] == [True, True, True]


def test_interactive_selection_returns_listed_webcam():
    selected = select_source(
        webcam_probe=lambda: [0, 2],
        file_picker=lambda: "unused.mp4",
        input_func=lambda _: "2",
    )

    assert selected == "webcam:2"


def test_interactive_selection_returns_file_dialog_path():
    selected = select_source(
        webcam_probe=lambda: [0],
        file_picker=lambda: "videos/test.mp4",
        input_func=lambda _: "2",
    )

    assert selected == "videos/test.mp4"


def test_cancelled_file_dialog_can_cancel_prompt():
    answers = iter(["1", ""])

    with pytest.raises(SourceSelectionCancelled):
        select_source(
            webcam_probe=lambda: [],
            file_picker=lambda: "",
            input_func=lambda _: next(answers),
        )


def test_cli_source_bypasses_interactive_selection(tmp_path, monkeypatch):
    config_path = tmp_path / "config.toml"
    config_path.write_text("[video]\nsource = \"\"\n[line]\npoint_a = [0.25, 0.5]\npoint_b = [0.75, 0.5]\nentry_direction = \"A_TO_B\"\n[display]\n", encoding="utf-8")

    def fail_select_source():
        raise AssertionError("select_source should not be called")

    monkeypatch.setattr(cli, "select_source", fail_select_source)

    settings = cli.resolve_runtime_settings(["--config", str(config_path), "--source", "webcam:0"])

    assert settings.video.source == "webcam:0"


def test_missing_source_calls_interactive_selection(tmp_path, monkeypatch):
    config_path = tmp_path / "config.toml"
    config_path.write_text("[video]\nsource = \"\"\n[line]\npoint_a = [0.25, 0.5]\npoint_b = [0.75, 0.5]\nentry_direction = \"A_TO_B\"\n[display]\n", encoding="utf-8")
    monkeypatch.setattr(cli, "select_source", lambda: "videos/test.mp4")

    settings = cli.resolve_runtime_settings(["--config", str(config_path)])

    assert settings.video.source == "videos/test.mp4"


def test_cli_open_failure_returns_clear_error(tmp_path, monkeypatch, capsys):
    config_path = tmp_path / "config.toml"
    config_path.write_text("[video]\nsource = \"\"\n[line]\npoint_a = [0.25, 0.5]\npoint_b = [0.75, 0.5]\nentry_direction = \"A_TO_B\"\n[display]\n", encoding="utf-8")

    monkeypatch.setattr(cli, "select_source", lambda: "webcam:999")
    monkeypatch.setattr(cli, "run", lambda settings: (_ for _ in ()).throw(VideoSourceError("fallback retry message")))

    exit_code = cli.main(["--config", str(config_path)])

    assert exit_code == 1
    assert "fallback retry message" in capsys.readouterr().err
