import argparse
import sys
import time
from cli_src import *
from src import file_in_memory

# In $PROFILE, add the following line to make the script available in PowerShell:
#   function erql {python "[path_to_script]" @args}

def main():
    raw_input = sys.argv[1:]
    if len(raw_input) == 0:
        print("No arguments provided. Please provide a command.")
        sys.exit(1)
    else:
        command = raw_input[0].split('-')
        return command

command = main()

def interpret(command):
    if command[0] == 'file':
        if command[1] == 'upload' or command[1] == 'select':
            from tkinter import filedialog
            from tkinter import Tk
            file_path = filedialog.askopenfilename()
            if file_path[-4:] == '.csv':
                file_in_memory.Filepath(file_path)
                print(f"File selected: {file_path}")
                check_c = input("Check content? Y/N: ")
                if check_c.upper() == 'Y':
                    import pandas as pd
                    df = pd.read_csv(file_path)
                    print("*" * 100) # For creating a delimitation between table head and other outputs in the terminal.
                    print(df.head())
                    print("*" * 100)
                else:
                    pass
            else:
                print("No file selected or wrong file format. Please upload a valid .csv file")


interpret(command)