#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Say  hello to optional argument")
parser.add_argument("-n",
                    "--name",
                    metavar="name",
                    default="world",
                    help="Name to greet")
args = parser.parse_args()
name = args.name
print("Hello " + name)
