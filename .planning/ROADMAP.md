# Roadmap: Controle de Presenca em Ambiente

**Created:** 2026-05-18
**Mode:** Vertical MVP
**Granularity:** Coarse

## Overview

The roadmap builds the counter as a working vertical slice first: video input and line calibration, then person observations, then the core tracking/counting behavior, then logs/validation, and finally runtime hardening.

## Phases

### Phase 1: Local Video Runner and Virtual Line
**Goal:** User can open webcam or video file, view frames, and configure/see the virtual line.
**Mode:** mvp
**Requirements:** VID-01, VID-02, VID-03, VID-04, CAL-01, CAL-02, CAL-03, CAL-04
**UI hint:** no
**Success Criteria:**
1. Running the app with a webcam source displays live frames with a visible virtual line.
2. Running the app with a video file displays frames until the file ends.
3. Invalid video sources fail with a clear message.
4. Line endpoints and direction can be configured and reused from a config file.
5. FPS or processing status is visible while the app runs.

### Phase 2: Person Observation Pipeline
**Goal:** User can run model inference and receive normalized person observations from each frame.
**Mode:** mvp
**Requirements:** OBS-01, OBS-02, OBS-03, OBS-04
**UI hint:** no
**Success Criteria:**
1. A model can be loaded through configuration or CLI settings.
2. Non-person detections/classes are filtered out.
3. Each accepted person observation includes confidence, bounding box and centroid.
4. Confidence threshold and resize settings can be changed without editing code.
5. The overlay can draw observed people for visual debugging.

### Phase 3: Tracking and Entry/Exit Counting
**Goal:** System tracks people across frames and counts entry/exit crossings exactly once per valid event.
**Mode:** mvp
**Requirements:** TRK-01, TRK-02, TRK-03, TRK-04, CNT-01, CNT-02, CNT-03, CNT-04, CNT-05
**UI hint:** no
**Success Criteria:**
1. Visible people receive stable temporary track IDs in simple scenes.
2. Short detection gaps do not immediately reset a person's track.
3. Noisy/unconfirmed tracks are ignored for counting.
4. Crossing the configured line increments either entry or exit based on direction.
5. A person lingering near the line is not repeatedly counted from jitter.
6. Current entry, exit and occupancy counts are drawn on the video.
7. Tracker boundaries allow a future ByteTrack adapter without rewriting counting logic.

### Phase 4: Event Logs and Validation Workflow
**Goal:** User can audit count events through logs and validate behavior with recorded videos.
**Mode:** mvp
**Requirements:** LOG-01, LOG-02, LOG-03, VAL-01, VAL-02
**UI hint:** no
**Success Criteria:**
1. Each valid crossing writes one CSV event row.
2. Event rows include timestamp, frame number, track ID, direction and current counters.
3. Stopping or finishing a run prints a clear summary.
4. A sample validation workflow documents how to test with webcam/celular videos.
5. Automated tests cover line geometry, crossing classification, duplicate protection and CSV logging.

### Phase 5: Real-Time Hardening and Handoff
**Goal:** The local counter is stable enough to use for demo/validation and ready for Phase 2 planning of advanced tracking.
**Mode:** mvp
**Requirements:** Supports all v1 requirements through polish, integration and documentation.
**UI hint:** no
**Success Criteria:**
1. The end-to-end app runs with both webcam and video file sources.
2. Runtime settings are documented with examples.
3. The app reports useful performance information and handles common camera/file failures.
4. The codebase documents where ByteTrack and model fine-tuning should plug in later.
5. Final verification confirms all v1 requirements are either complete or explicitly deferred with reason.

## Requirement Coverage

| Phase | Requirements |
|-------|--------------|
| Phase 1 | VID-01, VID-02, VID-03, VID-04, CAL-01, CAL-02, CAL-03, CAL-04 |
| Phase 2 | OBS-01, OBS-02, OBS-03, OBS-04 |
| Phase 3 | TRK-01, TRK-02, TRK-03, TRK-04, CNT-01, CNT-02, CNT-03, CNT-04, CNT-05 |
| Phase 4 | LOG-01, LOG-02, LOG-03, VAL-01, VAL-02 |
| Phase 5 | Integration, hardening and verification across all v1 requirements |

**Coverage:**
- v1 requirements: 26 total
- Requirements mapped to primary delivery phases: 26
- Unmapped: 0

## Phase Ordering Rationale

- Video input and calibration come first because every later phase needs repeatable frames and visible line geometry.
- Observation normalization comes before tracking so the counter is not tied to one model's output shape.
- Tracking/counting is isolated as the core value and highest-risk logic.
- Logs and validation follow the working counter so results become auditable.
- Performance and hardening happen last so optimization follows correctness.

---
*Roadmap created: 2026-05-18*
