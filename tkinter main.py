import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from collections import defaultdict
import erql
import interpreter



root = tk.Tk()
root.title('Tkinter GUI')
root.geometry('300x450')

text_box = scrolledtext.ScrolledText(root,width=30,height=20,highlightthickness=2, highlightbackground="gray",wrap=tk.WORD)
text_box.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

def return_val():
    if entry.get() == 'cv':
        interpreter.interpret(entry.get())
        for i in range(len(avg_table)):
            text_box.insert(tk.END, i)

    

entry = tk.Entry(root, width=20, font=("Consolas", 12))
entry.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

btn2 = tk.Button(root, text="Enter", command=return_val)
btn2.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

root.mainloop()

