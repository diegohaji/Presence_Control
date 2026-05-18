from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any
import tomllib


DEFAULT_CONFIG_PATH = Path("config.toml")
VALID_ENTRY_DIRECTIONS = {"A_TO_B", "B_TO_A"}

DEFAULT_CONFIG_TOML = """[video]
source = ""

[line]
point_a = [0.25, 0.50]
point_b = [0.75, 0.50]
entry_direction = "A_TO_B"

[display]
window_name = "Presence Control"
show_fps = true
"""


@dataclass(frozen=True)
class VideoConfig:
    source: str = ""


@dataclass(frozen=True)
class LineConfig:
    point_a: tuple[float, float] = (0.25, 0.50)
    point_b: tuple[float, float] = (0.75, 0.50)
    entry_direction: str = "A_TO_B"


@dataclass(frozen=True)
class DisplayConfig:
    window_name: str = "Presence Control"
    show_fps: bool = True


@dataclass(frozen=True)
class AppConfig:
    video: VideoConfig
    line: LineConfig
    display: DisplayConfig
    config_path: Path


def load_config(path: str | Path = DEFAULT_CONFIG_PATH) -> AppConfig:
    config_path = Path(path).resolve()
    if not config_path.exists():
        write_default_config(config_path)

    with config_path.open("rb") as config_file:
        data = tomllib.load(config_file)

    return parse_config(data, config_path)


def write_default_config(path: str | Path = DEFAULT_CONFIG_PATH) -> None:
    config_path = Path(path).resolve()
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(DEFAULT_CONFIG_TOML, encoding="utf-8")


def parse_config(data: dict[str, Any], config_path: Path) -> AppConfig:
    video_data = _section(data, "video")
    line_data = _section(data, "line")
    display_data = _section(data, "display")

    video = VideoConfig(source=str(video_data.get("source", "")))
    line = LineConfig(
        point_a=_parse_normalized_point(line_data.get("point_a", (0.25, 0.50)), "line.point_a"),
        point_b=_parse_normalized_point(line_data.get("point_b", (0.75, 0.50)), "line.point_b"),
        entry_direction=_parse_entry_direction(line_data.get("entry_direction", "A_TO_B")),
    )
    display = DisplayConfig(
        window_name=str(display_data.get("window_name", "Presence Control")),
        show_fps=bool(display_data.get("show_fps", True)),
    )
    return AppConfig(video=video, line=line, display=display, config_path=config_path)


def with_video_source(config: AppConfig, source: str) -> AppConfig:
    return replace(config, video=replace(config.video, source=source))


def _section(data: dict[str, Any], name: str) -> dict[str, Any]:
    value = data.get(name, {})
    if not isinstance(value, dict):
        raise ValueError(f"[{name}] must be a TOML table.")
    return value


def _parse_normalized_point(value: object, field_name: str) -> tuple[float, float]:
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError(f"{field_name} must contain two normalized numbers between 0.0 and 1.0.")

    try:
        x = float(value[0])
        y = float(value[1])
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field_name} must contain numeric normalized coordinates.") from exc

    if not 0.0 <= x <= 1.0 or not 0.0 <= y <= 1.0:
        raise ValueError(f"{field_name} coordinates must be normalized floats in the range 0.0 to 1.0.")
    return (x, y)


def _parse_entry_direction(value: object) -> str:
    direction = str(value)
    if direction not in VALID_ENTRY_DIRECTIONS:
        allowed = ", ".join(sorted(VALID_ENTRY_DIRECTIONS))
        raise ValueError(f"line.entry_direction must be one of: {allowed}.")
    return direction
