import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from collections import defaultdict
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

def stats_show():
    pass

def k_means(k_num, dataframe):
    df = dataframe
    k = k_num
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=k, random_state=0).fit(df)
    df['Cluster'] = kmeans.labels_
    

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

def upload_csv():
    from tkinter import filedialog
    file_open = filedialog.askopenfilename(title="Select a file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    return file_open
    

def upload_excel():
    from tkinter import filedialog
    file_open = filedialog.askopenfilename(title="Select a file", filetypes=(("Excel files", "*.xlsx *.xls"), ("All files", "*.*")))
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

def file_info():
    from tkinter import filedialog
    from pathlib import Path
    filepath = filedialog.askopenfilename()
    ext = Path(filepath).suffix
    if ext == ".csv":
        df = pd.read_csv(filepath)
        csv_info = f"File info: \n\n Rows: {df.shape[0]} \n Columns: {df.shape[1]} \n\n {df.dtypes}"
    else:
        csv_info = "Please select a .csv file.\n\n"
    return csv_info

def correlation(x, y, ax, rows):
    alpha = set_alpha_level(rows)
    plot = sns.regplot(x=x, y=y, line_kws={'color':'red', 'linewidth':1, 'linestyle':'--'}, ax=ax, scatter_kws={'alpha': set_alpha_level(rows), 's':30})
    return plot

def heatmap(df, ax):
    plot = sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
    return plot


def set_alpha_level(rows):
    if rows <= 10:
        return 1
    elif rows <= 30:
        return 0.7
    elif rows <= 50:
        return 0.5
    elif rows <= 100:
        return 0.2
    else:
        return 0.05