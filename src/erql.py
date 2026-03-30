import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from collections import defaultdict
import os
import utils.errors_messagebox as errors
import utils.file_anonymizer as anonym
import utils.entries_per_student as entries



def virtual_analyse(): # This functions if for parsing the data from a Google form that we use.
    from tkinter import filedialog
    file = filedialog.askopenfilename(title="Select a file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    #This part is for cleaning the data up before I do anything with it.
    df = pd.read_csv(file)
    df = df.drop(columns=["Timestamp","Alte mentiuni"])
    df = df.dropna()
    df = df.replace("Nu", 0)
    df = df.replace("Da", 2)
    df = df.replace("Partial", 1)
    scor_deprinderi = [1, 0.5, 1, 0.5, 2, 2, 1, 0.5, 1, 0.5]
    df["Total"] = df.iloc[:, 1:11].mul(scor_deprinderi).sum(axis=1)
    avg_table = (df.groupby(df.columns[0], as_index=False)["Total"].mean())
    avg_table["Total"] = avg_table["Total"] * 5
    return avg_table

def return_val(): #This does the same but for files uploaded into memory.
    virtual_analyse()

def scatter_plot(df, hor, ver):
    plt.scatter(df[hor], df[ver], marker='x', alpha=0.6)
    plt.xlabel(hor)
    plt.ylabel(ver)
    plt.show()
    
class File_Var:   # Experimenting with class instead of file or function to make it easier to manipulate data in two steps (upload file into program and then perform analysis on it, after being given some basic info such as column names). This is so that you don't need to write a long ERQL statement like 'standard>graph>scatter>student_churn_rate>year'. 
    def __init__(self, file):
        from tkinter import filedialog
        self.file = pd.read_csv(file)

def upload():
    from tkinter import filedialog
    file_open = filedialog.askopenfilename(title="Select a file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    file_object = File_Var(file_open)
    return file_object

def folder_info():
    from tkinter import filedialog
    global folder_path
    folder_path = filedialog.askdirectory()
    return folder_path

def show_head():
    folder = r""
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    for i, filename in enumerate(files, start=1):
        filepath = os.path.join(folder, filename)
        if filepath.endswith('.csv'):
            df = pd.read_csv(filepath)
            print(df.head())
        if filepath.endswith('.xlsx'):
            df = pd.read_excel(filepath)
            print(df.head())


