---
phase: 01-local-video-runner-and-virtual-line
status: human_needed
verified: 2026-05-18
plans:
  - 01-01
  - 01-02
  - 01-03
requirements_checked:
  - VID-01
  - VID-02
  - VID-03
  - VID-04
  - CAL-01
  - CAL-02
  - CAL-03
  - CAL-04
---

# Phase 01 Verification: Local Video Runner and Virtual Line

## Verdict

**Status:** human_needed

The Phase 1 implementation satisfies the planned code and artifact checks by inspection and compile validation. Full automated and smoke verification needs a Python 3.11+ environment with project dependencies installed.

## Must-Have Checks

| Requirement | Result | Evidence |
|-------------|--------|----------|
| VID-01 webcam source | PASS by implementation, smoke pending | `parse_source_spec("webcam:0")`, `open_capture()` and runner source flow exist. |
| VID-02 local video file | PASS by implementation, smoke pending | Non-empty non-webcam source strings are file paths and runner opens them through OpenCV. |
| VID-03 clear source errors | PASS by implementation | `VideoSourceError` messages include retry/fallback guidance and CLI prints them to stderr with non-zero exit. |
| VID-04 FPS/status visible | PASS by implementation, smoke pending | `draw_overlay()` writes FPS/status text and `runner.run()` prints terminal FPS/status. |
| CAL-01 configurable line | PASS | `[line].point_a` and `[line].point_b` load from TOML as normalized points. |
| CAL-02 configurable direction | PASS | `[line].entry_direction` validates `A_TO_B` or `B_TO_A`. |
| CAL-03 visible line/direction marker | PASS by implementation, smoke pending | `overlay.py` calls `cv2.line`, `cv2.arrowedLine`, and `cv2.putText`. |
| CAL-04 reusable config file | PASS | `load_config()` creates missing `config.toml` and reads TOML with stdlib `tomllib`. |

## Automated Checks

| Check | Result | Detail |
|-------|--------|--------|
| `python -m compileall presence_control` | PASS | All package modules compile. |
| `python -m pytest` | BLOCKED | Current shell uses Python 3.10.7 and has no `pytest` installed. |
| `python -m presence_control --help` | BLOCKED | Current shell uses Python 3.10.7, so stdlib `tomllib` is unavailable. |

## Human Verification Items

1. Run in Python 3.11+ with dev dependencies: `python -m pip install -e .[dev]`.
2. Run `python -m pytest`.
3. Run `python -m presence_control --help`.
4. Smoke test a webcam source: `python -m presence_control --source webcam:0`.
5. Smoke test one local video file: `python -m presence_control --source path/to/video.mp4`.

## Gaps

None found in implementation. Remaining items are environment and manual smoke checks.

---
*Verification created: 2026-05-18*
