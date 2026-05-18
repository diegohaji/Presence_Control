from __future__ import annotations

import argparse
from collections.abc import Sequence
import sys

from presence_control.config import DEFAULT_CONFIG_PATH, AppConfig, load_config, with_video_source
from presence_control.source_selector import select_source
from presence_control.video_source import VideoSourceError, open_capture, parse_source_spec


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="presence-control",
        description="Open a local video source and draw a configurable virtual line.",
    )
    parser.add_argument(
        "-c",
        "--config",
        default=str(DEFAULT_CONFIG_PATH),
        help="Path to the TOML config file. Created with defaults when missing.",
    )
    parser.add_argument(
        "-s",
        "--source",
        default=None,
        help='Video source, for example "webcam:0" or "path/to/video.mp4".',
    )
    return parser


def resolve_runtime_settings(argv: list[str] | None = None) -> AppConfig:
    args = build_parser().parse_args(argv)
    config = load_config(args.config)
    if args.source is not None:
        config = with_video_source(config, args.source)
    elif not config.video.source:
        config = with_video_source(config, select_source())
    return config


def main(argv: Sequence[str] | None = None) -> int:
    try:
        settings = resolve_runtime_settings(list(argv) if argv is not None else None)
        capture = open_capture(parse_source_spec(settings.video.source))
        capture.release()
        return 0
    except (VideoSourceError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
