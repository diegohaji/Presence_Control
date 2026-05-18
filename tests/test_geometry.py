from __future__ import annotations

from presence_control.config import AppConfig, DisplayConfig, LineConfig, VideoConfig
from presence_control.geometry import normalized_line_to_pixels, normalized_point_to_pixel
from presence_control import overlay


def test_normalized_point_to_pixel_uses_frame_dimensions():
    assert normalized_point_to_pixel((0.25, 0.50), 640, 480) == (160, 240)
    assert normalized_point_to_pixel((0.75, 0.50), 640, 480) == (480, 240)


def test_normalized_point_to_pixel_clamps_to_frame_bounds():
    assert normalized_point_to_pixel((1.0, 1.0), 640, 480) == (639, 479)


def test_direction_a_to_b_yields_arrow_from_a_to_b():
    line = normalized_line_to_pixels(LineConfig(entry_direction="A_TO_B"), (480, 640, 3))

    assert line.entry_start.label == "A"
    assert line.entry_end.label == "B"
    assert line.direction_label == "A->B"


def test_direction_b_to_a_yields_arrow_from_b_to_a():
    line = normalized_line_to_pixels(LineConfig(entry_direction="B_TO_A"), (480, 640, 3))

    assert line.entry_start.label == "B"
    assert line.entry_end.label == "A"
    assert line.direction_label == "B->A"


class FakeFrame:
    shape = (480, 640, 3)


class FakeCv2:
    FONT_HERSHEY_SIMPLEX = 1

    def __init__(self):
        self.calls = []

    def line(self, *args):
        self.calls.append(("line", args))

    def arrowedLine(self, *args, **kwargs):
        self.calls.append(("arrowedLine", args, kwargs))

    def putText(self, *args):
        self.calls.append(("putText", args))


def test_draw_overlay_draws_line_arrow_and_text(monkeypatch):
    fake_cv2 = FakeCv2()
    monkeypatch.setattr(overlay, "cv2", fake_cv2)
    config = AppConfig(
        video=VideoConfig(source="webcam:0"),
        line=LineConfig(),
        display=DisplayConfig(),
        config_path="config.toml",
    )
    frame = FakeFrame()

    returned = overlay.draw_overlay(frame, config, fps=12.3, status_text="Source: webcam:0")

    assert returned is frame
    assert any(call[0] == "line" for call in fake_cv2.calls)
    assert any(call[0] == "arrowedLine" for call in fake_cv2.calls)
    assert sum(1 for call in fake_cv2.calls if call[0] == "putText") >= 4
