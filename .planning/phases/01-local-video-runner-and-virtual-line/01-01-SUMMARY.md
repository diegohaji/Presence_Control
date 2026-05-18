---
phase: 01-local-video-runner-and-virtual-line
plan: "01"
subsystem: config-cli
tags: [python, argparse, tomllib, pytest, config]
requires: []
provides:
  - Python package scaffold with console entry point
  - TOML configuration loading and default generation
  - CLI parsing with source and config overrides
affects: [phase-01, video-source, runner]
tech-stack:
  added: [opencv-python, pytest]
  patterns: [dataclass-config, cli-over-config]
key-files:
  created:
    - pyproject.toml
    - README.md
    - presence_control/__init__.py
    - presence_control/__main__.py
    - presence_control/cli.py
    - presence_control/config.py
    - tests/test_config.py
  modified: []
key-decisions:
  - "Use frozen dataclasses for runtime configuration objects."
  - "Generate default TOML from a deterministic static template."
patterns-established:
  - "Configuration loads first, then CLI values override specific fields."
  - "Validation errors are raised at config boundaries with actionable messages."
requirements-completed: [CAL-01, CAL-02, CAL-04]
duration: 20min
completed: 2026-05-18
---

# Phase 01 Plan 01: Project Scaffold and Config Summary

**Python CLI scaffold with TOML-backed runtime settings and CLI-over-config source precedence**

## Performance

- **Duration:** 20 min
- **Started:** 2026-05-18T00:00:00Z
- **Completed:** 2026-05-18T00:20:00Z
- **Tasks:** 3
- **Files modified:** 7

## Accomplishments

- Created the installable `presence-control` package and `python -m presence_control` entry point.
- Added stdlib `tomllib` config loading with first-run default `config.toml` generation.
- Added CLI parsing for `--config`/`-c` and `--source`/`-s`, with CLI source values overriding config values.
- Added config tests for default generation, custom config paths, CLI overrides, coordinate validation and direction validation.

## Task Commits

1. **Tasks 1-3: Scaffold, config loading, CLI precedence and tests** - `8cc31cb` (feat)

## Files Created/Modified

- `pyproject.toml` - Python 3.11 package metadata, dependencies, pytest config and console script.
- `README.md` - Local install, test and initial run commands.
- `presence_control/__init__.py` - Package marker and version.
- `presence_control/__main__.py` - Module execution entry point.
- `presence_control/cli.py` - Argparse parser and runtime settings resolution.
- `presence_control/config.py` - Typed config model, TOML loader, default generation and validation.
- `tests/test_config.py` - Unit coverage for config and CLI precedence.

## Decisions Made

- Frozen dataclasses keep runtime settings explicit and easy to pass into later runner code.
- Default config generation is a static TOML template because `tomllib` is read-only.

## Deviations from Plan

None - plan executed exactly as written.

**Total deviations:** 0 auto-fixed.
**Impact on plan:** No scope change.

## Issues Encountered

- Local `python` is Python 3.10.7, so importing `tomllib` and running `python -m presence_control --help` cannot succeed in this shell. The project correctly declares Python 3.11+.
- `pytest` is not installed in the local Python 3.10 environment, so pytest verification could not be completed here.

## Verification

- PASS: `python -m compileall presence_control`
- BLOCKED LOCALLY: `python -m pytest tests/test_config.py -q` due to missing pytest and Python 3.10.
- BLOCKED LOCALLY: `python -m presence_control --help` due to Python 3.10 missing stdlib `tomllib`.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

The package scaffold and runtime settings model are ready for video source parsing, interactive selection and OpenCV capture handling.

---
*Phase: 01-local-video-runner-and-virtual-line*
*Completed: 2026-05-18*
