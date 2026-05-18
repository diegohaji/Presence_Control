# Phase 1 Research: Local Video Runner and Virtual Line

**Phase:** 01 - Local Video Runner and Virtual Line
**Researched:** 2026-05-18
**Confidence:** HIGH for APIs, MEDIUM for UX details

## Research Summary

Phase 1 should be implemented as a small local Python package with a CLI entry point, TOML configuration, OpenCV video capture, optional Tk file dialog for interactive file selection, and a display loop that draws the virtual line plus FPS/status overlays. There is no need for detection, tracking, segmentation, or counting in this phase.

The important architectural boundary is to keep configuration, source selection, video opening, geometry conversion, overlay rendering and the runner separate. Phase 2+ can then consume the same frame loop and config without rewriting user-facing source selection or line calibration.

## Technical Findings

### TOML Configuration

- Python 3.11 includes `tomllib` for reading TOML from binary file handles.
- `tomllib` is read-only, so default `config.toml` generation should be written as a deterministic string from our own code instead of adding a dependency just to write TOML.
- Use dataclasses or typed dictionaries to normalize config into application objects.
- Store line coordinates as normalized floats in `[line]` so the same config works across resolutions.

### OpenCV Video Capture

- `cv2.VideoCapture` supports both camera indexes and video file paths.
- Always check `isOpened()` immediately and fail with a clear message if the source cannot be opened.
- Read loop should handle `ret == false` as clean video end for files and as a capture failure for live sources.
- FPS measurement can be computed in the runner with `time.perf_counter()` and displayed on frame plus terminal.

### Interactive Source Selection

- CLI `--source` should bypass prompts entirely.
- For interactive mode, list camera indexes that can be opened during probing and also offer a file path option.
- Tkinter `filedialog.askopenfilename()` is suitable for native file selection in a local Python application. It should be isolated behind a function so headless/test environments can bypass it.

### Virtual Line Overlay

- Convert normalized endpoints `(x, y)` to pixel coordinates using current frame width and height.
- Draw endpoint labels `A` and `B`, a line segment, and an arrow/direction marker showing which crossing direction is entry.
- Direction should be config-driven, e.g. `entry_direction = "A_TO_B"` or `"B_TO_A"`.

### Testing Approach

- Tests should avoid requiring a real camera.
- Config parsing/default generation, source spec parsing, normalized coordinate conversion, and overlay geometry can be unit-tested directly.
- Video source opening can be tested with invalid sources and, later, small generated video fixtures.

## Recommended File Structure

```text
presence_control/
  __init__.py
  cli.py
  config.py
  geometry.py
  overlay.py
  runner.py
  source_selector.py
  video_source.py
tests/
  test_config.py
  test_geometry.py
  test_source_spec.py
pyproject.toml
README.md
config.toml
```

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Webcam probing hangs or is slow | Probe a small configurable index range and release captures immediately. |
| Tk file dialog breaks headless tests | Keep it isolated and do not call it from tests unless explicitly mocked. |
| TOML write support missing in stdlib | Generate default config from a static template string. |
| CLI/config precedence becomes ambiguous | Centralize resolution in `cli.py`: config loads first, CLI overrides second. |
| Overlay line behaves differently by resolution | Store normalized coordinates and test conversion to pixels. |

## Sources

- https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html - OpenCV `VideoCapture` behavior for cameras/files.
- https://docs.python.org/3.11/library/tomllib.html - Python 3.11 TOML parser.
- https://docs.python.org/3/library/dialog.html - Python Tkinter dialog modules, including file dialogs.

---
*Research completed inline because GSD subagents are not installed.*
