# Phase 1 Discussion Log

**Date:** 2026-05-17
**Mode:** Discuss phase — default interactive

## Areas Discussed

### 1. Video Source Selection
- **Q1:** How to choose between webcam and file?
  - Options: CLI args / Interactive prompt / Config file only
  - **Selected:** Interactive prompt
- **Q2:** Should CLI also be supported?
  - Options: Both / Interactive only
  - **Selected:** Both (CLI --source overrides prompt)
- **Q3:** How to pick a video file?
  - Options: Type path / File dialog
  - **Selected:** File dialog
- **Q4:** CLI with prompt — skip or confirm?
  - Options: Skip prompt entirely / Show confirmation
  - **Selected:** Skip prompt entirely
- **Q5:** First-run config generation?
  - Options: Auto-generate default / Built-in defaults only
  - **Selected:** Auto-generate default
- **Q6:** Webcam selection with multiple cameras?
  - Options: List available / Just ask for index
  - **Selected:** List available cameras
- **Q7:** Error message on source failure?
  - Options: One line + exit / Suggest fallback
  - **Selected:** Suggest fallback
- **Q8:** FPS display location?
  - Options: Overlay on frame / Terminal log / Both
  - **Selected:** Both

### 2. Configuration Format
- **Q1:** What config format?
  - Options: TOML / YAML / JSON
  - **Selected:** TOML
- **Q2:** Default config file location?
  - Options: config.toml in CWD / XDG standard path
  - **Selected:** config.toml in CWD
- **Q3:** Config path override + CLI/config interaction?
  - Options: CLI overrides config / Config overrides CLI
  - **Selected:** CLI overrides config (with --config/-c flag)
- **Q4:** Config sections for Phase 1?
  - Options: Flat keys / Sections for future growth
  - **Selected:** Sections ([video], [line], [display])
- **Q5:** Line coordinate format?
  - Options: Normalized 0-1 / Absolute pixels
  - **Selected:** Normalized 0-1
- **Q6:** Direction configuration approach?
  - Options: Named endpoints / Axis-based
  - **Selected:** Named endpoints
- **Q7:** CLI alias support?
  - Options: Yes, -c for --config / Full flags only
  - **Selected:** Yes (-c alias accepted)