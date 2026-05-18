from __future__ import annotations

from collections.abc import Callable

try:
    import cv2
except ImportError:  # pragma: no cover - exercised only when OpenCV is not installed locally.
    cv2 = None  # type: ignore[assignment]

from presence_control.video_source import VideoSourceError


class SourceSelectionCancelled(VideoSourceError):
    """Raised when the user cancels interactive source selection."""


def probe_webcams(max_index: int = 5) -> list[int]:
    if cv2 is None:
        return []

    available: list[int] = []
    for index in range(max_index):
        capture = cv2.VideoCapture(index)
        try:
            if capture.isOpened():
                available.append(index)
        finally:
            capture.release()
    return available


def choose_video_file() -> str:
    from tkinter import Tk, filedialog

    root = Tk()
    root.withdraw()
    try:
        selected = filedialog.askopenfilename(
            title="Choose a video file",
            filetypes=[
                ("Video files", "*.mp4 *.avi *.mov *.mkv *.webm"),
                ("All files", "*.*"),
            ],
        )
    finally:
        root.destroy()
    return selected or ""


def select_source(
    *,
    webcam_probe: Callable[[], list[int]] = probe_webcams,
    file_picker: Callable[[], str] = choose_video_file,
    input_func: Callable[[str], str] = input,
) -> str:
    webcams = webcam_probe()

    while True:
        print("Available video sources:")
        for option_number, webcam_index in enumerate(webcams, start=1):
            print(f"{option_number}. Webcam {webcam_index} (webcam:{webcam_index})")
        file_option = len(webcams) + 1
        print(f"{file_option}. Choose local video file")

        choice = input_func("Select source: ").strip()
        if not choice:
            raise SourceSelectionCancelled("Source selection cancelled. Choose a webcam or local video file to continue.")

        if choice.isdigit():
            choice_number = int(choice)
            if 1 <= choice_number <= len(webcams):
                return f"webcam:{webcams[choice_number - 1]}"
            if choice_number == file_option:
                selected_file = file_picker()
                if selected_file:
                    return selected_file
                print("No file selected. Choose another source or press Enter to cancel.")
                continue

        print("Invalid source choice. Select a listed webcam number or the video file option.")
