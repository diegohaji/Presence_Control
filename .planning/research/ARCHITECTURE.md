# Architecture Research

**Domain:** Local real-time computer vision counter
**Researched:** 2026-05-18
**Confidence:** MEDIUM

## Recommended Architecture

Use a modular frame-processing pipeline:

1. **VideoSource** - opens webcam or file and yields frames with frame index/timestamp.
2. **DetectorSegmenter** - returns person observations as masks or boxes with confidence.
3. **ObservationNormalizer** - converts masks/boxes into centroids and bounding boxes.
4. **Tracker** - assigns stable temporary IDs across frames.
5. **LineCounter** - detects signed line crossings and updates counts.
6. **OverlayRenderer** - draws line, tracks, IDs and counters.
7. **EventLogger** - writes entry/exit events and final summary.
8. **Runner/CLI** - wires config, source, model, display and output.

## Data Flow

```text
VideoSource -> DetectorSegmenter -> ObservationNormalizer -> Tracker -> LineCounter -> OverlayRenderer
                                                                       -> EventLogger
```

## Key Interfaces

### Observation

```text
frame_id
confidence
bbox: x1, y1, x2, y2
centroid: x, y
mask: optional
```

### Track

```text
track_id
centroid_history
bbox
age
missed_frames
confirmed
last_counted_crossing
```

### CountEvent

```text
timestamp
frame_id
track_id
direction: entry|exit
line_id
entry_count
exit_count
occupancy_estimate
```

## Design Notes

- Keep detection independent from tracking. This lets the project start with centroid tracking and later add ByteTrack without rewriting counting.
- Keep line geometry independent from video IO. Geometry should be unit-tested without camera access.
- Treat segmentation masks as optional. The counter needs stable centroids and boxes; masks are useful when available but should not be required everywhere.
- Persist runtime settings in a config file. Different rooms and camera angles will need different line points and thresholds.

## Failure Modes to Design Around

- Person hovers on the line, causing repeated crossing events.
- Person disappears for a few frames and receives a new ID.
- Two people overlap and swap IDs.
- Camera angle makes entry/exit direction ambiguous.
- Model detects posters/reflections or partial bodies as people.

## Roadmap Implications

- Phase 1 should build VideoSource, config and overlay before model complexity.
- Phase 2 should create detector/normalizer boundaries and at least one baseline model path.
- Phase 3 should make tracker and line-crossing logic reliable with tests.
- Phase 4 should add logs and evaluation.
- Phase 5 should optimize and polish runtime behavior.

## Sources

- https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html - capture API and frame loop behavior.
- https://segmentation-models-pytorch.readthedocs.io/en/latest/ - segmentation model family and encoders.
- https://arxiv.org/abs/2110.06864 - ByteTrack association strategy.

---
*Architecture research completed: 2026-05-18*
