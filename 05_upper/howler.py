#!/usr/bin/env python3

import argparse
import os
import sys

def get_args():
    parser = argparse.ArgumentParser(description="Change font to uppercase")
    parser.add_argument("text", metavar="text", type=str, help="text to be changed")
    parser.add_argument("-o", "--outfile", metavar="outfile", type=str, help="optional output file")
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args

def main():
    args = get_args()
    fh = open(args.outfile, "wt") if args.outfile else sys.stdout
    fh.write(args.text.upper() + "\n")
    fh.close()



if __name__ == "__main__":
    main()

