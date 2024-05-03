#!/usr/bin/env python3
import argparse


def test_pos_arg():
    parser = argparse.ArgumentParser(
        description="Testing position arg",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("word", metavar="word", help="This word is parsed")
    return parser.parse_args()


def main():
    args = test_pos_arg()
    word = args.word
    article = "an" if word.lower()[0] in "aeiou" else "a"

    print(f"There is {article} {word}")


if __name__ == "__main__":
    main()
