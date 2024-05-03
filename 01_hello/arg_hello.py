#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Say Hello to an argument")
parser.add_argument("name", help="Name to greet")
parser.add_argument("last_name", help="Last Name to greet")
args = parser.parse_args()
name = args.name
last_name = args.last_name
print("Hello " + name + " " + last_name)
