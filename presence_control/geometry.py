from __future__ import annotations

from dataclasses import dataclass

from presence_control.config import LineConfig


@dataclass(frozen=True)
class PixelPoint:
    label: str
    x: int
    y: int

    @property
    def xy(self) -> tuple[int, int]:
        return (self.x, self.y)


@dataclass(frozen=True)
class PixelLine:
    point_a: PixelPoint
    point_b: PixelPoint
    entry_start: PixelPoint
    entry_end: PixelPoint
    direction_label: str


def normalized_point_to_pixel(point: tuple[float, float], width: int, height: int) -> tuple[int, int]:
    if width <= 0 or height <= 0:
        raise ValueError("Frame width and height must be positive.")

    x = round(point[0] * width)
    y = round(point[1] * height)
    return (_clamp(x, 0, width - 1), _clamp(y, 0, height - 1))


def normalized_line_to_pixels(line_config: LineConfig, frame_shape: tuple[int, ...]) -> PixelLine:
    height, width = int(frame_shape[0]), int(frame_shape[1])
    point_a_xy = normalized_point_to_pixel(line_config.point_a, width, height)
    point_b_xy = normalized_point_to_pixel(line_config.point_b, width, height)
    point_a = PixelPoint(label="A", x=point_a_xy[0], y=point_a_xy[1])
    point_b = PixelPoint(label="B", x=point_b_xy[0], y=point_b_xy[1])

    entry_start, entry_end = entry_direction_points(line_config.entry_direction, point_a, point_b)
    return PixelLine(
        point_a=point_a,
        point_b=point_b,
        entry_start=entry_start,
        entry_end=entry_end,
        direction_label=f"{entry_start.label}->{entry_end.label}",
    )


def entry_direction_points(
    entry_direction: str,
    point_a: PixelPoint,
    point_b: PixelPoint,
) -> tuple[PixelPoint, PixelPoint]:
    if entry_direction == "A_TO_B":
        return (point_a, point_b)
    if entry_direction == "B_TO_A":
        return (point_b, point_a)
    raise ValueError("entry_direction must be A_TO_B or B_TO_A.")


def _clamp(value: int, lower: int, upper: int) -> int:
    return max(lower, min(value, upper))
