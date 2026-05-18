from __future__ import annotations

import argparse
from collections.abc import Sequence

from presence_control.config import DEFAULT_CONFIG_PATH, AppConfig, load_config, with_video_source


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
    return config


def main(argv: Sequence[str] | None = None) -> int:
    resolve_runtime_settings(list(argv) if argv is not None else None)
    return 0
