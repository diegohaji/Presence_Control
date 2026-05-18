<!-- GSD:project-start source:PROJECT.md -->
## Project

**Controle de Presenca em Ambiente**

Um sistema de visao computacional para detectar pessoas em video, rastrear seus deslocamentos e contar entradas e saidas quando elas cruzam uma linha virtual. O projeto deve funcionar tanto com webcam quanto com arquivo de video, sem assumir um unico tipo de ambiente: porta, corredor, catraca ou sala ampla podem ser usados como cenarios de validacao.

O entregavel inicial e um contador em tempo real com sobreposicao visual e log de eventos de entrada/saida. A prioridade e contagem correta; desempenho em tempo real vem logo em seguida.

**Core Value:** Contar corretamente entradas e saidas de pessoas ao cruzarem uma linha virtual em video, registrando cada evento de forma auditavel.

### Constraints

- **Tech stack**: Python, OpenCV, PyTorch e segmentation_models_pytorch - estas tecnologias foram indicadas na ideia inicial.
- **Video input**: Webcam e arquivo local - ambos foram confirmados para o primeiro entregavel.
- **Counting model**: Linha virtual com direcao - e o mecanismo central do produto.
- **Tracking**: Comecar simples com centroid tracking e manter interface para ByteTrack - reduz risco inicial e preserva caminho de melhoria.
- **Dataset**: COCO e videos proprios - COCO ajuda com classe pessoa; videos proprios validam o ambiente real.
- **Priority**: Correcao da contagem antes de FPS - evita otimizar uma contagem errada.
- **Privacy**: Nao armazenar identidade pessoal - logs devem registrar eventos de contagem, nao identidade.
<!-- GSD:project-end -->

<!-- GSD:stack-start source:research/STACK.md -->
## Technology Stack

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
- Use a single virtual line and centroid crossing.
- Because trajectories are constrained and easiest to validate.
- Use stricter track confirmation, longer disappearance tolerance and optional ByteTrack.
- Because occlusion and diagonal movement increase ID switches.
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
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

Conventions not yet established. Will populate as patterns emerge during development.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

Architecture not yet mapped. Follow existing patterns found in the codebase.
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/`, or `.codex/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->



<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
