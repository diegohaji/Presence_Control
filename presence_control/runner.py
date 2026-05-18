from __future__ import annotations

import time

try:
    import cv2
except ImportError:  # pragma: no cover - exercised only when OpenCV is not installed locally.
    cv2 = None  # type: ignore[assignment]

from presence_control.config import AppConfig
from presence_control.overlay import draw_overlay
from presence_control.video_source import VideoSourceError, open_capture, parse_source_spec


def run(settings: AppConfig) -> int:
    if cv2 is None:
        raise VideoSourceError("OpenCV is not installed. Install project dependencies and retry.")

    source_spec = parse_source_spec(settings.video.source)
    capture = open_capture(source_spec)
    frame_count = 0
    fps = 0.0
    last_frame_time = time.perf_counter()
    last_log_time = 0.0

    try:
        while True:
            ok, frame = capture.read()
            if not ok:
                status = "Video ended" if source_spec.kind == "file" else "No frame from live source"
                if settings.display.show_fps:
                    print(f"{status}. Frames: {frame_count}, FPS: {fps:.1f}")
                break

            now = time.perf_counter()
            elapsed = now - last_frame_time
            last_frame_time = now
            if elapsed > 0:
                fps = 1.0 / elapsed

            frame_count += 1
            status_text = f"Source: {source_spec.display_name}"
            draw_overlay(frame, settings, fps, status_text)
            cv2.imshow(settings.display.window_name, frame)

            if settings.display.show_fps and (frame_count == 1 or now - last_log_time >= 1.0):
                print(f"Frame {frame_count} | FPS: {fps:.1f} | {status_text}")
                last_log_time = now

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                if settings.display.show_fps:
                    print(f"Stopped by user. Frames: {frame_count}, FPS: {fps:.1f}")
                break
        return 0
    finally:
        capture.release()
        cv2.destroyAllWindows()
