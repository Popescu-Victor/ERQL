import tkinter as tk
import pandas as pd
from tkinter import scrolledtext
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict


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

btn = tk.Button(root, text="ENTER")
btn.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

root.mainloop()
