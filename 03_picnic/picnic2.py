#!/usr/bin/env python3
import argparse

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='item',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()


def main():
    args = get_args()
    items = args.item

    num = len(items)

    if args.sorted:
        items.sort()

    bringing = ""
    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = f"{items[0]} and {items[1]}"
    else:
        bringing = f"{', '.join(items[:-1])}, and {items[-1]}"
    print(f"You are bringing {bringing}.")

if __name__ == "__main__":
    main()
