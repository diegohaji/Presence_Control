from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

try:
    import cv2
except ImportError:  # pragma: no cover - exercised only when OpenCV is not installed locally.
    cv2 = None  # type: ignore[assignment]


class VideoSourceError(RuntimeError):
    """Raised when a configured video source cannot be parsed or opened."""


@dataclass(frozen=True)
class SourceSpec:
    kind: Literal["webcam", "file"]
    value: int | Path
    raw: str

    @property
    def display_name(self) -> str:
        return f"webcam:{self.value}" if self.kind == "webcam" else str(self.value)


def parse_source_spec(value: str) -> SourceSpec:
    source = value.strip()
    if not source:
        raise VideoSourceError(
            "Video source is empty. Choose a webcam like 'webcam:0' or a local video file path."
        )

    if source.startswith("webcam:"):
        index_text = source.removeprefix("webcam:").strip()
        if not index_text.isdigit():
            raise VideoSourceError(
                f"Invalid webcam source '{source}'. Use a numeric camera index, for example 'webcam:0'."
            )
        return SourceSpec(kind="webcam", value=int(index_text), raw=source)

    return SourceSpec(kind="file", value=Path(source), raw=source)


def open_capture(spec: SourceSpec) -> Any:
    if cv2 is None:
        raise VideoSourceError(
            "OpenCV is not installed. Install project dependencies, then retry the webcam or video file."
        )

    capture_arg = spec.value if spec.kind == "webcam" else str(spec.value)
    capture = cv2.VideoCapture(capture_arg)
    if capture.isOpened():
        return capture

    capture.release()
    raise VideoSourceError(_open_failure_message(spec))


def _open_failure_message(spec: SourceSpec) -> str:
    if spec.kind == "webcam":
        return (
            f"Could not open source '{spec.display_name}'. "
            "Try another camera index such as 'webcam:1', check camera permissions, or choose a video file."
        )
    return (
        f"Could not open source '{spec.display_name}'. "
        "Check that the file path exists and is a supported video, or retry with a webcam source like 'webcam:0'."
    )
