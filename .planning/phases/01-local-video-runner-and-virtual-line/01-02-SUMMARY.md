---
phase: 01-local-video-runner-and-virtual-line
plan: "02"
subsystem: video-source
tags: [python, opencv, webcam, video-file, cli]
requires:
  - phase: 01-local-video-runner-and-virtual-line
    provides: TOML config and CLI settings from 01-01
provides:
  - Source spec parser for webcam and file inputs
  - OpenCV capture wrapper with actionable source errors
  - Interactive webcam/file selection boundary
affects: [phase-01, runner]
tech-stack:
  added: []
  patterns: [source-parser, mockable-selector, cli-error-boundary]
key-files:
  created:
    - presence_control/source_selector.py
    - presence_control/video_source.py
    - tests/test_source_spec.py
  modified:
    - presence_control/cli.py
    - tests/test_config.py
key-decisions:
  - "Keep OpenCV imports tolerant so pure unit tests and compile checks do not require camera hardware."
  - "Keep the interactive selector injectable for tests and headless environments."
patterns-established:
  - "Source strings are parsed before opening captures."
  - "CLI catches source errors and returns a non-zero exit code with stderr guidance."
requirements-completed: [VID-01, VID-02, VID-03]
duration: 25min
completed: 2026-05-18
---

# Phase 01 Plan 02: Video Source Selection Summary

**Webcam/file source parsing with mockable interactive selection and OpenCV capture error handling**

## Performance

- **Duration:** 25 min
- **Started:** 2026-05-18T00:20:00Z
- **Completed:** 2026-05-18T00:45:00Z
- **Tasks:** 3
- **Files modified:** 5

## Accomplishments

- Added `SourceSpec`, `parse_source_spec()` and `open_capture()` for `webcam:N` and file path inputs.
- Added webcam probing, Tk file dialog isolation and terminal source selection without import-time side effects.
- Wired CLI resolution so explicit `--source` bypasses prompts while empty config sources invoke interactive selection.
- Added source tests covering parsing, OpenCV failure release, interactive selection and CLI error conversion.

## Task Commits

1. **Tasks 1-3: Parse/open sources, interactive selection and CLI wiring** - `3b6fb0c` (feat)

## Files Created/Modified

- `presence_control/video_source.py` - Source parsing and OpenCV capture opening.
- `presence_control/source_selector.py` - Webcam probing and file-dialog-backed interactive selection.
- `presence_control/cli.py` - Source selection precedence and source-open error boundary.
- `tests/test_source_spec.py` - Unit tests for source behavior without camera hardware.
- `tests/test_config.py` - Adjusted default-generation coverage to avoid prompting.

## Decisions Made

- OpenCV capture objects are released immediately on failed `isOpened()` checks and during webcam probing.
- `select_source()` accepts injectable probe, file-picker and input callables to keep tests deterministic.

## Deviations from Plan

None - plan executed exactly as written.

**Total deviations:** 0 auto-fixed.
**Impact on plan:** No scope change.

## Issues Encountered

- Local pytest verification remains blocked because the available `python` is 3.10.7 and has no `pytest`; the code still compiles in this shell.

## Verification

- PASS: `python -m compileall presence_control`
- BLOCKED LOCALLY: `python -m pytest tests/test_config.py tests/test_source_spec.py -q` due to missing pytest and Python 3.10.
- STATIC PASS: source files contain `cv2.VideoCapture`, prompt bypass coverage, retry/fallback errors and release calls.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Source parsing and capture opening are ready for the display runner and overlay loop.

---
*Phase: 01-local-video-runner-and-virtual-line*
*Completed: 2026-05-18*
