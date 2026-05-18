from __future__ import annotations

import pytest

from presence_control.cli import resolve_runtime_settings
from presence_control.config import DEFAULT_CONFIG_TOML, load_config


def test_missing_default_config_is_generated(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    config = load_config()

    generated = tmp_path / "config.toml"
    assert generated.exists()
    assert "[video]" in generated.read_text(encoding="utf-8")
    assert "[line]" in generated.read_text(encoding="utf-8")
    assert "[display]" in generated.read_text(encoding="utf-8")
    assert config.config_path == generated
    assert config.line.point_a == (0.25, 0.50)
    assert config.line.point_b == (0.75, 0.50)
    assert config.line.entry_direction == "A_TO_B"


def test_custom_config_path_is_read(tmp_path):
    custom_config = tmp_path / "custom.toml"
    custom_config.write_text(
        DEFAULT_CONFIG_TOML.replace('source = ""', 'source = "videos/test.mp4"'),
        encoding="utf-8",
    )

    config = resolve_runtime_settings(["-c", str(custom_config)])

    assert config.config_path == custom_config
    assert config.video.source == "videos/test.mp4"


def test_cli_source_overrides_config_source(tmp_path):
    config_path = tmp_path / "config.toml"
    config_path.write_text(
        DEFAULT_CONFIG_TOML.replace('source = ""', 'source = "videos/test.mp4"'),
        encoding="utf-8",
    )

    config = resolve_runtime_settings(["--config", str(config_path), "--source", "webcam:0"])

    assert config.video.source == "webcam:0"


def test_source_short_flag_overrides_config_source(tmp_path):
    config_path = tmp_path / "config.toml"
    config_path.write_text(DEFAULT_CONFIG_TOML, encoding="utf-8")

    config = resolve_runtime_settings(["-c", str(config_path), "-s", "webcam:0"])

    assert config.video.source == "webcam:0"


def test_normalized_coordinates_must_be_between_zero_and_one(tmp_path):
    config_path = tmp_path / "bad.toml"
    config_path.write_text(
        DEFAULT_CONFIG_TOML.replace("point_a = [0.25, 0.50]", "point_a = [1.25, 0.50]"),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="normalized"):
        load_config(config_path)


def test_entry_direction_must_be_named_endpoint_direction(tmp_path):
    config_path = tmp_path / "bad.toml"
    config_path.write_text(
        DEFAULT_CONFIG_TOML.replace('entry_direction = "A_TO_B"', 'entry_direction = "LEFT"'),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="entry_direction"):
        load_config(config_path)
