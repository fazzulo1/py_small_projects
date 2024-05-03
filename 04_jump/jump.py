#!/usr/bin/env python3

import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description="Changes phone number", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("text", metavar="text", help="phone number")
    return parser.parse_args()


def main():
    args = get_args()
    text = args.text
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}
    print("".join([jumper.get(t, t) for t in text]))

if __name__ == "__main__":
    main()
