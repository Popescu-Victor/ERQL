#!/usr/bin/env python3
# cli.py

import argparse
import sys


def parse_ui():
    user_input = input("Write your ERQL script here: ")
    commands = user_input.split(">")
    return commands

command_list = parse_ui()

def interpret(commands):
    if commands[0] == "file":
        if commands[1] == "upload":
            from tkinter import filedialog
            file = filedialog.askopenfilename(title="Select a file to upload")
            print(f"File uploaded: {file}")

interpret(command_list)