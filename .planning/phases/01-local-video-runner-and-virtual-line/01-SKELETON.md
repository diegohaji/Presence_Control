# Walking Skeleton - Controle de Presenca em Ambiente

**Phase:** 1
**Generated:** 2026-05-18

## Capability Proven End-to-End

A user can start a local Python app, choose webcam or video file input, see live frames with a configured virtual line and direction marker, and observe FPS/status feedback.

## Architectural Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Runtime | Python 3.11+ local CLI package | Matches OpenCV/PyTorch ecosystem and enables stdlib `tomllib`. |
| Video I/O | OpenCV `cv2.VideoCapture` | Supports both camera indexes and local video file paths. |
| Configuration persistence | `config.toml` in current working directory | Matches D-08 and keeps first-run setup visible/editable. |
| Config parser | stdlib `tomllib` plus generated TOML template string | Matches D-07 without adding a write dependency. |
| User interaction | CLI flags first, interactive prompt/file dialog fallback | Matches D-01 through D-04 while preserving automation. |
| Display surface | OpenCV window with overlay | Gives immediate visual validation of line geometry. |
| Directory layout | `presence_control/` package plus `tests/` | Keeps phase outputs simple and ready for Phase 2 model integration. |

## Stack Touched in Phase 1

- [ ] Project scaffold: `pyproject.toml`, package directory, pytest test suite.
- [ ] Routing/entry point: `python -m presence_control` or configured console script.
- [ ] Persistence: first-run `config.toml` generation and TOML read path.
- [ ] UI interaction: CLI source selection, optional file dialog, OpenCV display window.
- [ ] Local deployment: documented install and run commands in `README.md`.

## Out of Scope (Deferred to Later Slices)

- Person detection, segmentation, tracking and counting.
- ByteTrack integration.
- COCO dataset loading or model fine-tuning.
- CSV entry/exit logs.
- Web dashboard or cloud deployment.
- Ground-truth evaluation workflow.

## Subsequent Slice Plan

- Phase 2: Add person observation pipeline on top of the video runner.
- Phase 3: Add tracking and entry/exit counting using the configured line.
- Phase 4: Add event logs and repeatable validation workflow.
- Phase 5: Harden real-time behavior and document advanced-tracking handoff.
