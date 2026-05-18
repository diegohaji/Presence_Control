# Project Research Summary

**Project:** Controle de Presenca em Ambiente
**Domain:** Computer vision people counting with virtual line crossing
**Researched:** 2026-05-18
**Confidence:** MEDIUM

## Executive Summary

The project is best built as a local Python computer-vision pipeline rather than as a single monolithic script. The stable core is not the model itself; it is the chain from video input to person observation, tracking, signed line crossing, visual overlay and event logging.

The recommended approach is to start with OpenCV video input, a configurable virtual line, normalized person observations and centroid tracking. segmentation_models_pytorch can serve the segmentation path, while the architecture should keep detector output normalized so ByteTrack can be added later if crowded scenes or ID switches become the limiting factor.

The largest risk is incorrect counting from jitter, ID switches or ambiguous line direction. The roadmap should therefore validate geometry and tracking behavior before spending too much effort on training or UI polish.

## Key Findings

### Recommended Stack

Python, OpenCV, PyTorch and segmentation_models_pytorch match the user's proposed materials. OpenCV VideoCapture covers webcam and file input, segmentation_models_pytorch provides common segmentation architectures/encoders, and COCO provides person-class annotations for baseline model work and validation.

**Core technologies:**
- Python: application runtime and CLI.
- OpenCV: video capture, frame display, drawing and overlays.
- PyTorch: model runtime.
- segmentation_models_pytorch: segmentation model experiments.
- COCO: person-class dataset and validation source.

### Expected Features

**Must have:**
- Webcam and video-file input.
- Configurable virtual line and direction.
- Person detection/segmentation adapter.
- Temporary tracking IDs.
- Entry/exit counting with duplicate protection.
- Real-time overlay.
- CSV event log.

**Should have:**
- Recorded validation videos.
- FPS display.
- Testable geometry/tracking logic.

**Defer:**
- ByteTrack adapter.
- Interactive calibration.
- ROI masks.
- Ground-truth metrics.
- Model fine-tuning workflow.

### Architecture Approach

Use a pipeline of small components: VideoSource, DetectorSegmenter, ObservationNormalizer, Tracker, LineCounter, OverlayRenderer, EventLogger and CLI runner. This keeps the count logic testable and prevents model-specific details from leaking through the application.

### Critical Pitfalls

1. **Counting detections instead of crossings** - count only signed track crossings.
2. **Double counting near the line** - use movement thresholds and cooldown.
3. **Wrong direction mapping** - make line direction visible/configurable.
4. **ID switches under occlusion** - start simple and add ByteTrack when needed.
5. **Segmentation/tracking output mismatch** - normalize masks/boxes before tracking.

## Implications for Roadmap

### Phase 1: Local Video Runner and Calibration
**Rationale:** Establish source handling, frame loop, config and overlay before model complexity.
**Delivers:** Webcam/file input, line config and visual debug runner.
**Addresses:** Video input and calibration.

### Phase 2: Person Observation Pipeline
**Rationale:** Create the detector/segmentation boundary and normalize model output.
**Delivers:** Person observations with centroid/bbox and confidence filtering.
**Uses:** OpenCV, PyTorch, segmentation_models_pytorch/COCO-compatible model outputs.

### Phase 3: Tracking and Line Counting
**Rationale:** This is the core value and highest-risk logic.
**Delivers:** Centroid tracker, crossing detection, direction classification and duplicate protection.

### Phase 4: Logging and Validation
**Rationale:** Logs and repeatable videos make the counter auditable.
**Delivers:** CSV log, run summary and sample validation workflow.

### Phase 5: Real-Time Polish and Hardening
**Rationale:** Optimize only after the count is correct.
**Delivers:** FPS tuning, CLI polish, error handling and documented next steps for ByteTrack.

### Research Flags

Phases likely needing deeper research during planning:
- **Phase 2:** Model selection and exact segmentation/detection output format.
- **Phase 5:** ByteTrack adapter and performance tuning.

Phases with standard patterns:
- **Phase 1:** OpenCV capture and overlay.
- **Phase 3:** Geometry and centroid tracking can be implemented locally with tests.
- **Phase 4:** CSV logging and validation scripts.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | MEDIUM | Official docs confirm core APIs; exact package versions should be pinned during implementation. |
| Features | HIGH | Features follow directly from user scope and line-counting domain. |
| Architecture | HIGH | Pipeline boundary is standard for CV applications and keeps risk isolated. |
| Pitfalls | MEDIUM | Common MOT/counting issues are known, but severity depends on real videos. |

**Overall confidence:** MEDIUM

### Gaps to Address

- Exact baseline model: decide during Phase 2 whether the first runnable detector is segmentation_models_pytorch-based or a simpler pretrained person detector.
- Validation videos: collect short videos for porta/corredor/sala-style scenes.
- Performance target: set FPS target after the first working pipeline exists.

## Sources

### Primary
- https://segmentation-models-pytorch.readthedocs.io/en/latest/ - model architectures and encoders.
- https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html - camera/file capture.
- https://cocodataset.org/ - COCO dataset and tasks.
- https://arxiv.org/abs/2110.06864 - ByteTrack paper.
- https://github.com/FoundationVision/ByteTrack - reference ByteTrack implementation.

---
*Research completed: 2026-05-18*
*Ready for roadmap: yes*
