#!/usr/bin/env python3
"""Meme Sprint 3 entry: copy the pre-rendered meme to the output dir.

The meme itself (entry.png, 1024x1024, drawn with Pillow by gen.py)
ships in this repository; this entrypoint is stdlib-only so it runs
in the grader's bare Python 3.13 image. It copies entry.png to
MAKEFUN_OUTPUT_DIR/entry.png (fallback /output), emptying the output
directory's contents first -- never the directory itself.
"""
import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png missing from repository", file=sys.stderr)
        return 1
    if os.path.getsize(src) > 1_048_576:
        print("entry.png exceeds the 1 MiB gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    print("wrote", os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
