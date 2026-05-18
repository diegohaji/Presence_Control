---
phase: 01-local-video-runner-and-virtual-line
plan: "03"
subsystem: runner-overlay
tags: [python, opencv, geometry, fps, overlay]
requires:
  - phase: 01-local-video-runner-and-virtual-line
    provides: Config and source opening from 01-01 and 01-02
provides:
  - Normalized line-to-pixel geometry helpers
  - OpenCV overlay drawing for line, endpoint labels, direction and FPS/status
  - Frame runner that opens sources, displays frames and releases resources
affects: [phase-01, phase-02, observations]
tech-stack:
  added: []
  patterns: [geometry-helper, overlay-renderer, runner-loop]
key-files:
  created:
    - presence_control/geometry.py
    - presence_control/overlay.py
    - presence_control/runner.py
    - tests/test_geometry.py
  modified:
    - README.md
    - presence_control/cli.py
    - tests/test_source_spec.py
key-decisions:
  - "Represent converted line endpoints with labeled PixelPoint and PixelLine dataclasses."
  - "Treat file EOF as a clean stop and release capture/window resources in a finally block."
patterns-established:
  - "Runner owns frame loop and lifecycle; overlay owns drawing; geometry owns coordinate conversion."
  - "FPS/status is emitted both to the frame overlay and terminal when display.show_fps is enabled."
requirements-completed: [VID-04, CAL-03]
duration: 25min
completed: 2026-05-18
---

# Phase 01 Plan 03: Runner and Overlay Summary

**OpenCV frame loop with normalized virtual line, entry-direction arrow and FPS/status feedback**

## Performance

- **Duration:** 25 min
- **Started:** 2026-05-18T00:45:00Z
- **Completed:** 2026-05-18T01:10:00Z
- **Tasks:** 3
- **Files modified:** 7

## Accomplishments

- Added normalized point and line conversion helpers with direction labels for `A_TO_B` and `B_TO_A`.
- Added overlay rendering for line, endpoint labels, direction arrow, FPS and source/status text.
- Added the display runner with capture open, read loop, `cv2.imshow`, `q` exit handling and cleanup in `finally`.
- Updated CLI to run the display loop and README with webcam, video-file and custom-config examples.

## Task Commits

1. **Tasks 1-3: Geometry, overlay, runner and CLI wiring** - `699d57b` (feat)

## Files Created/Modified

- `presence_control/geometry.py` - Normalized coordinate conversion and entry-direction helpers.
- `presence_control/overlay.py` - OpenCV drawing for the Phase 1 visual diagnostics.
- `presence_control/runner.py` - Frame loop connecting source capture, overlay and display cleanup.
- `presence_control/cli.py` - Calls the runner after settings resolution.
- `README.md` - Documents webcam, file, config and normalized line usage.
- `tests/test_geometry.py` - Unit coverage for geometry and overlay drawing calls.
- `tests/test_source_spec.py` - Updated CLI failure test for runner-level source errors.

## Decisions Made

- The runner returns `0` on normal stop conditions including file EOF and user `q`.
- Overlay remains limited to Phase 1 diagnostics; no detection, tracking, segmentation or counting behavior was added.

## Deviations from Plan

None - plan executed exactly as written.

**Total deviations:** 0 auto-fixed.
**Impact on plan:** No scope change.

## Issues Encountered

- Local pytest verification remains blocked because the available `python` is 3.10.7 and has no `pytest`.
- Manual webcam/video smoke tests were not run from this shell because OpenCV dependencies and Python 3.11 are not installed locally.

## Verification

- PASS: `python -m compileall presence_control`
- BLOCKED LOCALLY: `python -m pytest` due to missing pytest and Python 3.10.
- BLOCKED LOCALLY: `python -m presence_control --help` due to Python 3.10 missing stdlib `tomllib`.
- NOT RUN: Manual webcam/video smoke test.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Phase 1 now provides a local runner surface that Phase 2 can reuse for person observation overlays and model inference.

---
*Phase: 01-local-video-runner-and-virtual-line*
*Completed: 2026-05-18*
