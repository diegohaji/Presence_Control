from __future__ import annotations

from typing import Any

try:
    import cv2
except ImportError:  # pragma: no cover - exercised only when OpenCV is not installed locally.
    cv2 = None  # type: ignore[assignment]

from presence_control.config import AppConfig
from presence_control.geometry import normalized_line_to_pixels


LINE_COLOR = (0, 255, 255)
ARROW_COLOR = (0, 200, 0)
TEXT_COLOR = (255, 255, 255)
SHADOW_COLOR = (0, 0, 0)


def draw_overlay(frame: Any, config: AppConfig, fps: float, status_text: str) -> Any:
    if cv2 is None:
        raise RuntimeError("OpenCV is required to draw the video overlay.")

    pixel_line = normalized_line_to_pixels(config.line, frame.shape)
    cv2.line(frame, pixel_line.point_a.xy, pixel_line.point_b.xy, LINE_COLOR, 2)

    cv2.putText(frame, "A", _label_origin(pixel_line.point_a.xy), cv2.FONT_HERSHEY_SIMPLEX, 0.7, TEXT_COLOR, 2)
    cv2.putText(frame, "B", _label_origin(pixel_line.point_b.xy), cv2.FONT_HERSHEY_SIMPLEX, 0.7, TEXT_COLOR, 2)

    cv2.arrowedLine(
        frame,
        pixel_line.entry_start.xy,
        pixel_line.entry_end.xy,
        ARROW_COLOR,
        2,
        tipLength=0.12,
    )

    status = f"{status_text} | entry {pixel_line.direction_label}"
    fps_text = f"FPS: {fps:.1f}"
    _draw_text(frame, fps_text, (12, 28))
    _draw_text(frame, status, (12, 58))
    return frame


def _label_origin(point: tuple[int, int]) -> tuple[int, int]:
    return (point[0] + 6, max(18, point[1] - 8))


def _draw_text(frame: Any, text: str, origin: tuple[int, int]) -> None:
    cv2.putText(frame, text, origin, cv2.FONT_HERSHEY_SIMPLEX, 0.7, SHADOW_COLOR, 4)
    cv2.putText(frame, text, origin, cv2.FONT_HERSHEY_SIMPLEX, 0.7, TEXT_COLOR, 2)
