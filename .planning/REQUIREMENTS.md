# Requirements: Controle de Presenca em Ambiente

**Defined:** 2026-05-18
**Core Value:** Contar corretamente entradas e saidas de pessoas ao cruzarem uma linha virtual em video, registrando cada evento de forma auditavel.

## v1 Requirements

### Video Input

- [x] **VID-01**: User can run the counter using a webcam source.
- [x] **VID-02**: User can run the counter using a local video file.
- [x] **VID-03**: User receives a clear error when the selected video source cannot be opened.
- [ ] **VID-04**: User can see live frames with current FPS or processing status.

### Calibration

- [x] **CAL-01**: User can configure a virtual line using two frame coordinates.
- [x] **CAL-02**: User can configure which crossing direction means entry and which means exit.
- [ ] **CAL-03**: User can see the virtual line and direction marker overlaid on the video.
- [x] **CAL-04**: User can reuse line and runtime settings through a config file.

### Person Observation

- [ ] **OBS-01**: User can load a person detection or segmentation model for inference.
- [ ] **OBS-02**: System filters model output to person observations only.
- [ ] **OBS-03**: System converts each person observation into a centroid and bounding box.
- [ ] **OBS-04**: User can tune confidence and frame-size settings without code changes.

### Tracking

- [ ] **TRK-01**: System assigns a temporary track ID to each visible person.
- [ ] **TRK-02**: System keeps a track alive across short detection gaps.
- [ ] **TRK-03**: System avoids counting unconfirmed/noisy tracks.
- [ ] **TRK-04**: System exposes a tracker interface that can later support ByteTrack.

### Counting

- [ ] **CNT-01**: System detects when a tracked person crosses the configured virtual line.
- [ ] **CNT-02**: System classifies each crossing as entry or exit based on configured direction.
- [ ] **CNT-03**: System increments entry and exit counters exactly once per valid crossing event.
- [ ] **CNT-04**: System protects against duplicate counts caused by jitter near the line.
- [ ] **CNT-05**: User can see current entry, exit and estimated occupancy counts in the overlay.

### Logging and Validation

- [ ] **LOG-01**: System writes each valid crossing event to a CSV log.
- [ ] **LOG-02**: Each log event includes timestamp, frame number, track ID, direction and current counters.
- [ ] **LOG-03**: User receives a final run summary after the video ends or the run is stopped.
- [ ] **VAL-01**: User can validate the pipeline with short recorded videos from webcam or celular.
- [ ] **VAL-02**: Geometry, counting and logging behavior are covered by automated tests that do not require a camera.

## v2 Requirements

### Advanced Tracking

- **ADV-01**: User can enable a ByteTrack tracker adapter for harder scenes.
- **ADV-02**: System reports basic tracking diagnostics such as missed frames and ID switches.

### Calibration UX

- **UX-01**: User can set the virtual line by clicking on the frame.
- **UX-02**: User can define a region of interest to ignore irrelevant areas.

### Evaluation

- **EVAL-01**: User can compare counted events against a manual ground-truth annotation file.
- **EVAL-02**: System can export an annotated output video for review.

### Model Workflow

- **ML-01**: User can fine-tune or evaluate a segmentation model using COCO/person labels and videos proprios.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Face recognition or identity tracking | The project counts movement, not identity. |
| Multi-camera synchronization | Not needed for the first working counter and greatly increases complexity. |
| Cloud dashboard | Logs and local overlay are enough for v1 validation. |
| Access-control hardware integration | Outside the vision-counting core. |
| Training a model from scratch | Too much setup before validating the line-counting product. |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| VID-01 | Phase 1 | Complete |
| VID-02 | Phase 1 | Complete |
| VID-03 | Phase 1 | Complete |
| VID-04 | Phase 1 | Pending |
| CAL-01 | Phase 1 | Complete |
| CAL-02 | Phase 1 | Complete |
| CAL-03 | Phase 1 | Pending |
| CAL-04 | Phase 1 | Complete |
| OBS-01 | Phase 2 | Pending |
| OBS-02 | Phase 2 | Pending |
| OBS-03 | Phase 2 | Pending |
| OBS-04 | Phase 2 | Pending |
| TRK-01 | Phase 3 | Pending |
| TRK-02 | Phase 3 | Pending |
| TRK-03 | Phase 3 | Pending |
| TRK-04 | Phase 3 | Pending |
| CNT-01 | Phase 3 | Pending |
| CNT-02 | Phase 3 | Pending |
| CNT-03 | Phase 3 | Pending |
| CNT-04 | Phase 3 | Pending |
| CNT-05 | Phase 3 | Pending |
| LOG-01 | Phase 4 | Pending |
| LOG-02 | Phase 4 | Pending |
| LOG-03 | Phase 4 | Pending |
| VAL-01 | Phase 4 | Pending |
| VAL-02 | Phase 4 | Pending |

**Coverage:**
- v1 requirements: 26 total
- Mapped to phases: 26
- Unmapped: 0

---
*Requirements defined: 2026-05-18*
*Last updated: 2026-05-18 after roadmap creation*
