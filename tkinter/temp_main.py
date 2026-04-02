import tkinter as tk
import pandas as pd
from tkinter import scrolledtext
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict
from ERQL.src import errors_messagebox
from utils import validate_files, entried_per_student
from src import interpreter, erql


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

def enter(): # Just proof of concept for the time being. Later on I'll replace the many if-statements below with a hashmap.
    user_input = entry.get()
    rendered = interpreter.Render(user_input)
    if rendered.subj == "standard":
        if rendered.verb == "plot":
            fig = erql.scatter_plot(rendered.mod[0], rendered.mod[1])
            print('returned fig')
            canvas_widget = FigureCanvasTkAgg(fig, master=canvas1)
            canvas_widget.draw()
            canvas_widget.get_tk_widget().pack(fill="both", expand=True)
            
        if rendered.verb == "clear":
            text_box.delete('1.0', tk.END)
            
        if rendered.verb == "upload":
            uploaded_file = erql.upload()
            file_info = f"Column Names: \n *************** \n {uploaded_file.file.columns.tolist()}"
            text_box.insert(tk.END, file_info)
            if rendered.subj == "file":
                pass
                    
        if rendered.verb == "plot":
            for widget in canvas1.winfo_children():
                widget.destroy()
            fig = erql.scatter_file(rendered.mod[0], rendered.mod[1])
            canvas_widget = FigureCanvasTkAgg(fig, master=canvas1)
            canvas_widget.draw()
            canvas_widget.get_tk_widget().pack(fill="both", expand=True)

    if rendered.subj == "groups":
        if rendered.verb == "display":
            conn = sqlite3.connect("db.sqlite")
            cursor = conn.cursor()
            for row in cursor.execute("SELECT * FROM users"):
                text_box.insert(tk.END, row)

def on_enter(*args):
    enter()
    
entry.bind('<Return>', on_enter)

btn = tk.Button(root, text="ENTER")
btn.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

root.mainloop()







