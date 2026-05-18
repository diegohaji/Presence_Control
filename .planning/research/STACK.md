# Stack Research

**Domain:** Computer vision people counting with virtual line crossing
**Researched:** 2026-05-18
**Confidence:** MEDIUM

## Recommended Stack

### Core Technologies

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Python | 3.11+ | Application runtime | Strong ecosystem for OpenCV, PyTorch, model inference and scripts. |
| OpenCV | 4.x | Video capture, display, drawing, frame processing | Official VideoCapture supports cameras and video files, matching both required inputs. |
| PyTorch | 2.x | Model inference/training runtime | Required base for segmentation_models_pytorch and common tracking/detection stacks. |
| segmentation_models_pytorch | latest stable | Segmentation model library | Provides common segmentation architectures and encoders for person-mask experiments. |
| COCO Dataset | 2017/2020 tasks | Dataset and class taxonomy | Provides person annotations for detection/segmentation validation. |

### Supporting Libraries

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| NumPy | latest stable | Geometry and vector operations | Centroids, line crossing tests, frame arrays. |
| pandas or csv stdlib | latest/stdlib | Event logs | Use stdlib CSV for minimal v1; pandas only if analysis grows. |
| ByteTrack | implementation-specific | Multi-object tracking | Use after detector outputs stable bounding boxes and centroid tracker limits are visible. |
| pytest | latest stable | Automated tests | Geometry, tracker state and log behavior should be testable without video UI. |

### Development Tools

| Tool | Purpose | Notes |
|------|---------|-------|
| venv/requirements.txt | Dependency management | Simple enough for a local CV prototype. |
| CLI config file | Runtime configuration | Store video source, line endpoints, direction, confidence thresholds and output paths. |
| sample videos folder | Repeatable validation | Keep short videos for regression checks. |

## Installation

```bash
python -m venv .venv
pip install opencv-python torch torchvision segmentation-models-pytorch numpy pytest
```

ByteTrack should be added only when the detector/tracker boundary is clear, because available Python packages vary by implementation.

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| Centroid tracker first | ByteTrack first | Use ByteTrack first if the detector is already box-based and crowded scenes are common. |
| OpenCV HighGUI/local display | Web dashboard | Use a dashboard after the counter is correct and logs are stable. |
| segmentation_models_pytorch | Ultralytics/YOLO detector | Use YOLO if real-time person detection matters more than segmentation masks. |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| Training from scratch for v1 | Adds dataset, labeling and compute burden before proving the line-counting logic | Pretrained/fine-tuned model and recorded validation videos. |
| Counting raw detections per frame | Produces double counts and no direction | Track IDs and count only line crossings. |
| Hard-coded line coordinates | Breaks across camera angles | Runtime config or interactive calibration. |

## Stack Patterns by Variant

**If the source is a fixed doorway/corridor:**
- Use a single virtual line and centroid crossing.
- Because trajectories are constrained and easiest to validate.

**If the source is a wide room:**
- Use stricter track confirmation, longer disappearance tolerance and optional ByteTrack.
- Because occlusion and diagonal movement increase ID switches.

**If segmentation masks are noisy:**
- Convert masks to person bounding boxes/centroids and keep tracking logic independent.
- Because the counter only needs stable position history, not perfect pixel masks.

## Version Compatibility

| Package A | Compatible With | Notes |
|-----------|-----------------|-------|
| segmentation_models_pytorch | PyTorch/torchvision | Pin versions during implementation after local install is verified. |
| OpenCV | OS camera backend | Windows webcams may require backend tuning if default capture fails. |
| ByteTrack implementations | Detector output format | Needs bounding boxes, scores and class IDs. |

## Sources

- https://segmentation-models-pytorch.readthedocs.io/en/latest/ - official architecture/encoder documentation.
- https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html - official VideoCapture documentation for files and cameras.
- https://arxiv.org/abs/2110.06864 - ByteTrack paper.
- https://github.com/FoundationVision/ByteTrack - reference ByteTrack implementation.
- https://cocodataset.org/ - official COCO dataset site.

---
*Stack research for: people counting with virtual line crossing*
*Researched: 2026-05-18*
