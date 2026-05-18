# Pitfalls Research

**Domain:** People counting by virtual line crossing
**Researched:** 2026-05-18
**Confidence:** MEDIUM

## Critical Pitfalls

### 1. Counting detections instead of crossings

Counting every detected person per frame inflates totals immediately. The system must count only track-level transitions across the line.

**Mitigation:** Keep per-track previous/current side of the line and record a count event only when the side changes with sufficient movement.

### 2. Double counting while a person stands near the line

Small detection jitter can make a centroid bounce across the line.

**Mitigation:** Add minimum movement, track confirmation and cooldown after a crossing.

### 3. Wrong direction mapping

The same geometric crossing can mean entry or exit depending on camera placement.

**Mitigation:** Store line direction in config and expose it visually in the overlay.

### 4. ID switches during occlusion

If two people overlap, centroid tracking can swap IDs or create new tracks.

**Mitigation:** Start with simple scenes for v1, add disappearance tolerance, and keep ByteTrack as a planned adapter for harder scenes.

### 5. Model output mismatch

segmentation_models_pytorch produces segmentation-style outputs, while ByteTrack expects detection boxes/scores.

**Mitigation:** Normalize all model outputs into a common Observation structure before tracking.

### 6. Performance bottleneck from model inference

Real-time display can stall if inference is too slow.

**Mitigation:** Measure FPS, allow frame resizing/skipping, and separate correctness validation from optimization.

### 7. Privacy creep

Presence counting can accidentally drift into identity tracking.

**Mitigation:** Log track IDs only as temporary runtime identifiers and avoid storing faces or identity data.

## Testing Risks

- A passing demo on one webcam does not prove line counting works elsewhere.
- Video files are needed for repeatable regression tests.
- Geometry and tracking tests should run without GUI or camera hardware.

## Sources

- https://arxiv.org/abs/2110.06864 - tracking-by-detection context and MOT challenges.
- https://github.com/FoundationVision/ByteTrack - reference implementation expectations.
- https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html - capture behavior and backend considerations.

---
*Pitfalls research completed: 2026-05-18*
