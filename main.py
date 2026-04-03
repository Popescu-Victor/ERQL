import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from src import interpreter
from src import commands
from src import erql
from pathlib import Path
import pandas as pd

root = tk.Tk()
root.title("'Non Comissioned' Organizational Tools")
root.geometry("800x600")
root.columnconfigure(0, weight=8)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)

text_box = scrolledtext.ScrolledText(root,width=30,height=20,highlightthickness=2, highlightbackground="gray",wrap=tk.WORD)
text_box.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

canvas1 = tk.Frame(root,bg = "lightgray")
canvas1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

text_box2 = entry = tk.Entry(root, font=("Consolas", 16))
text_box2.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

def enter(*args): 
    user_input = entry.get()
    parsed_input = interpreter.Parsed_input(user_input)
    if parsed_input.subject == "file":
        if parsed_input.verb == "upload":
            if not parsed_input.obj or parsed_input.obj[0] == "csv":
                file_path_var = erql.upload_csv()
                df = pd.read_csv(file_path_var)
                file_info_text = (f"Filepath: {file_path_var} \n \n Columns: {df.columns.tolist()}")
                text_box.insert(tk.END, file_info_text)
entry.bind('<Return>', enter)

btn = tk.Button(root, text="ENTER")
btn.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

root.mainloop()
