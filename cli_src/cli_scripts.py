import pandas as pd
import sys


def ask_input():
    return input(">  ")

def interpret_input(user_input):
    if not isinstance(user_input, str) or ">" not in user_input:
        print("Invalid input format.")
        return None
    return user_input.split(">")

def main():
    while True:
        user_input = ask_input()
        if user_input.lower() == "exit":
            print("Exiting the program.")
            sys.exit(0)
        else:
            split_commands = interpret_input(user_input)
            print(split_commands)

main()