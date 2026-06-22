import pandas as pd
import sys


def ask_input():
    return input(">  ")

def interpret_input(user_input):
    try:
        return user_input.split(">")
    except:
        print("Invalid input format.")
        return None

def main():
    while True:
        user_input = ask_input()
        if user_input.lower() == "exit":
            print("Exiting the program.")
            sys.exit(0)
        else:
            interpret_input(user_input)

main()