#!/usr/bin/env python3
# cli.py
import sys

raw_input = sys.argv[1:]
if len(raw_input) == 0:
    print("No arguments provided. Please provide a command.")
    sys.exit(1)
else:
    command = raw_input[0]
    print(f"Command received: {command}")