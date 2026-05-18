# Feature Research

**Domain:** People counting by virtual line crossing
**Researched:** 2026-05-18
**Confidence:** MEDIUM

## Feature Categories

### Video Input

**Table stakes:**
- Webcam source selection.
- Local video file source.
- Frame read loop with graceful end/error handling.
- FPS measurement for runtime feedback.

**Differentiators:**
- Recorded output video with overlays.
- Multiple camera backend options.

### Calibration

**Table stakes:**
- Virtual line defined by two points.
- Direction mapping for entry vs exit.
- Persistent config so the line can be reused.

**Differentiators:**
- Interactive click-to-set line.
- Region of interest mask to ignore irrelevant areas.

### Person Detection / Segmentation

**Table stakes:**
- Person-only filtering.
- Confidence threshold.
- Consistent centroid or box extraction from model output.

**Differentiators:**
- segmentation_models_pytorch model path for person masks.
- Detector abstraction to swap segmentation, bounding-box detection or future models.

### Tracking

**Table stakes:**
- Temporary ID assignment.
- Handling short disappearance.
- Track confirmation before counting.
- Duplicate-count protection per track.

**Differentiators:**
- ByteTrack adapter.
- Track quality metrics and ID switch diagnostics.

### Counting

**Table stakes:**
- Line crossing test based on previous and current centroid positions.
- Direction classification.
- Separate in/out counters.
- Total occupancy estimate derived from entries minus exits.

**Differentiators:**
- Configurable cooldown per track.
- Zone-based count validation.

### Logging and Evaluation

**Table stakes:**
- CSV log with timestamp, track ID, direction, frame number and counters.
- Summary printed at run end.
- Sample validation videos.

**Differentiators:**
- Manual ground-truth annotation file.
- Precision/recall style counting metrics.

## Recommended v1 Scope

- Webcam and video-file input.
- Static configurable line.
- Person detection/segmentation adapter with at least one runnable baseline.
- Centroid tracker.
- Entry/exit counting with duplicate protection.
- Real-time overlay and CSV log.
- Short validation workflow using recorded videos.

## Recommended v2 Scope

- ByteTrack adapter.
- Interactive line calibration.
- ROI masks.
- Output video recording.
- Ground-truth comparison reports.
- Model fine-tuning workflow with COCO/videos proprios.

## Out of Scope for v1

- Face recognition.
- Multi-camera fusion.
- Production dashboard.
- Access-control hardware integration.
- Training a custom segmentation model from scratch.

## Sources

- https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html - video input capabilities.
- https://arxiv.org/abs/2110.06864 - ByteTrack tracking-by-detection approach.
- https://cocodataset.org/ - dataset tasks and annotations.

---
*Feature research completed: 2026-05-18*
