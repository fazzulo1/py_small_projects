#!/usr/bin/env python3

import argparse
import random
import os
import string

def get_args():
    parser = argparse.ArgumentParser(description="replace characters", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("text", metavar="text", type=str, help="text input")
    parser.add_argument("-s", "--seed", metavar="seed", type=int, help="seed number", default=None)
    parser.add_argument("-m", "--mutations", metavar="mutations", type=float, help="mutation number", default=0.1)

    args = parser.parse_args()

    if not 0 <= args.mutations < 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

def main():
    args = get_args()
    random.seed(args.seed)
    text = args.text
    new_text = list(text)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    len_text = len(text)
    num_mutations = round(args.mutations * len_text)
    index = random.sample(range(len_text), num_mutations)
    for i in index:
        new_text[i] = random.choice(alpha.replace(new_text[i], " "))

    print('You said: "{}"\nI heard : "{}"'.format(text, ''.join(new_text)))


if __name__ == "__main__":
    main()