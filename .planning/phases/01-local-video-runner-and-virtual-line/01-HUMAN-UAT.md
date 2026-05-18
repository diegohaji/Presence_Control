---
status: partial
phase: 01-local-video-runner-and-virtual-line
source:
  - 01-VERIFICATION.md
started: 2026-05-18
updated: 2026-05-18
---

# Phase 01 Human UAT

## Current Test

Awaiting Python 3.11+ dependency and video smoke verification.

## Tests

### 1. Install and test with Python 3.11+
expected: `python -m pip install -e .[dev]` succeeds and `python -m pytest` passes.
result: pending

### 2. CLI help works
expected: `python -m presence_control --help` shows `--source`, `-s`, `--config`, and `-c`.
result: pending

### 3. Webcam smoke test
expected: `python -m presence_control --source webcam:0` opens frames with the configured line, direction marker and FPS/status overlay.
result: pending

### 4. Local video file smoke test
expected: `python -m presence_control --source path/to/video.mp4` displays frames until EOF and exits cleanly.
result: pending

## Summary

total: 4
passed: 0
issues: 0
pending: 4
skipped: 0
blocked: 0

## Gaps
