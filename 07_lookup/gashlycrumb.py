#!/usr/bin/env python3

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Dictionary lookup")
    parser.add_argument("letter", metavar="letter", nargs="+", type=str, help="chars to lookup")
    parser.add_argument("-f", "--file", metavar="File", type=argparse.FileType("r"), default="gashlycrumb.txt", help="Files to lookup")
    return parser.parse_args()


def main():
    args = get_args()
    lookup = {line[0].upper(): line.rstrip() for line in args.file}

    for letter in args.letter:
        print({lookup.get(letter.upper(), f'I do not know "{letter}')})


if __name__ == "__main__":
    main()
