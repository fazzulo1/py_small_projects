#!/usr/bin/env python3

import argparse
import os


def get_args():
    parser = argparse.ArgumentParser(
        description="Change vowels",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("text", metavar="text", help="text to be chnaged")
    parser.add_argument(
        "-v",
        "--vowel",
        choices=list("aeiou"),
        metavar="vowel",
        type=str,
        default="a",
        help="replacement vowel",
    )
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def main():
    args = get_args()
    text = args.text
    vowel = args.vowel
    text = [
        vowel if c in "aeiou" else vowel.upper() if c in "AEIOU" else c
        for c in args.text
    ]
    print("".join(text))


if __name__ == "__main__":
    main()
