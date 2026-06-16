#!/usr/bin/env python3
# cli.py

import argparse
import sys


def interpret():
    user_input = input("Write your ERQL script here: ")
    commands = user_input.split(">")
    print(f"Commands: {commands}")

interpret()