#!/usr/bin/env python3

import argparse
import random

def get_args():
    parser = argparse.ArgumentParser(description="insult creator", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--number", metavar="number", type=int, default=3, help="number of insults")
    parser.add_argument("-a", "--adjectives", metavar="adjectives", type=int, default=2, help="number of adjectives")
    parser.add_argument("-s", "--seed", metavar="seed", type=int, default=None, help="seed")
    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')
    return args


def main():
    args = get_args()
    random.seed(args.seed)
    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.split()

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.split()

    for ins in range(args.number):
        adj =  ", ".join(random.sample(adjectives, k=args.adjectives))
        print(f"{adj} {random.choice(nouns)}")

if __name__ == "__main__":
    main()
