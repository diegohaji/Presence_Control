# Presence Control

Local computer-vision prototype for opening webcam or video-file sources and drawing a configurable virtual line before detection, tracking, and counting are added.

## Install

```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -e .[dev]
```

## Test

```bash
python -m pytest
python -m compileall presence_control
```

## Run

Use a webcam:

```bash
python -m presence_control --source webcam:0
```

Use a custom configuration file:

```bash
python -m presence_control --config config.toml
```

The first run creates `config.toml` if it does not exist. Edit `[line]` to adjust normalized coordinates and the entry direction:

```toml
[line]
point_a = [0.25, 0.50]
point_b = [0.75, 0.50]
entry_direction = "A_TO_B"
```
