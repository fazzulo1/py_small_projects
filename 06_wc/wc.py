#!/usr/bin/env python3

import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser(description="application to count wordsin  a file", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("file", metavar="file", nargs="*", type=argparse.FileType("rt"), default=[sys.stdin], help="files to be parsed")
    return parser.parse_args()


def main():
    args = get_args()
    total_lines, total_chars, total_words = 0, 0, 0
    for fh in args.file:
        num_lines = 0
        num_chars = 0
        num_words = 0
        for line in fh:
            num_lines = num_lines + 1
            num_chars = num_chars + len(line)
            num_words = num_words + len(line.split())

        total_lines = total_lines + num_lines
        total_chars = total_chars + num_chars
        total_words = total_words + num_words

        print(f"{num_lines:8}{num_words:8}{num_chars:8} {fh.name}")

    if len(args.file) > 1:
        print(f"{total_lines:8} {total_words:8} {total_chars:8}")


if __name__ == "__main__":
    main()
