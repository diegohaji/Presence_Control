# Phase 1: Local Video Runner and Virtual Line - Context

**Gathered:** 2026-05-17
**Status:** Ready for planning

<domain>
## Phase Boundary

Delivers the video I/O layer (webcam + local file), reusable TOML config system, interactive source selection, and visible virtual line overlay with direction markers. No detection, tracking, or counting in this phase — just frame acquisition, display, and line configuration.

Requirements: VID-01 through VID-04, CAL-01 through CAL-04.
</domain>

<decisions>
## Implementation Decisions

### Video Source Selection
- **D-01:** Interactive prompt at startup shows available sources — file dialog for video files, camera listing for webcams
- **D-02:** CLI `--source` / `-s` flag overrides the prompt entirely (no confirmation)
- **D-03:** `--source webcam:0` or `--source path/to/video.mp4` syntax
- **D-04:** If source fails to open, show clear error + suggest fallback/retry
- **D-05:** First run auto-generates a default `config.toml` if none exists
- **D-06:** FPS displayed both as on-frame overlay and printed to terminal log

### Configuration Format
- **D-07:** TOML using stdlib `tomllib` (Python 3.11+)
- **D-08:** Default file: `config.toml` in current working directory
- **D-09:** `--config` / `-c` flag to override config path
- **D-10:** CLI args override config values (not vice versa)
- **D-11:** Sections structured for future growth: `[video]`, `[line]`, `[display]`
- **D-12:** Line coordinates as normalized 0–1 floats (resolution-independent)
- **D-13:** Line direction configured via named endpoints (e.g., A→B = entry, B→A = exit)

### the agent's Discretion
- Overlay visual style (colors, font, line thickness)
- Specific TOML key names within sections
- Checkpoint/checkpoint file naming and structure
- Prompt wording and confirmation dialogues
</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Requirements
- `.planning/REQUIREMENTS.md` — VID-01/02/03/04, CAL-01/02/03/04 requirements
- `.planning/ROADMAP.md` — Phase 1 goal, success criteria, phase ordering rationale

### Project Context
- `.planning/PROJECT.md` — Core value, constraints, key decisions
- `.planning/STATE.md` — Current project state and workflow preferences

No external specs or ADRs exist yet.
</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- None — greenfield project. No existing code to reuse.

### Established Patterns
- None — patterns will be established in this phase.

### Integration Points
- None — this is the foundation phase. Outputs: frame pipeline and config system consumed by Phase 2+.
</code_context>

<specifics>
## Specific Ideas

No specific requirements — open to standard approaches.
</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.
</deferred>

---

*Phase: 1-Local Video Runner and Virtual Line*
*Context gathered: 2026-05-17*