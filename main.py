import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from src import interpreter
from src import commands
from src import erql
from pathlib import Path
import pandas as pd
import openpyxl
import seaborn as sns
from src import errors_messagebox as error
from utils.help import help_text
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from src import file_in_memory as fim

root = tk.Tk()
root.title("Educational Reporting Query Language")
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

text_box.insert(tk.END, "Welcome to ERQL! If this is your first time using this app, write 'help>' in the field at the bottom left corner of the window.\n\n")

def enter(*args):
    global selected_file 
    user_input = entry.get()
    parsed_input = interpreter.Parsed_input(user_input)
    if parsed_input.subject == "help":
        if parsed_input.verb =="":
            text_box.insert(tk.END, help_text)
        elif parsed_input.verb == "file":
            pass
        elif parsed_input.verb == "graph":
            pass
        elif parsed_input.verb == "virtual_class":
            pass
        elif parsed_input.verb == "homework" or parsed_input.verb == "hw":
            from utils import help
            text_box.insert(tk.END, help.help_homework)
        elif parsed_input.verb == "standard":
            pass
        elif parsed_input.verb == "group" or parsed_input.verb == "groups":
            pass

    elif parsed_input.subject == "file":

        if parsed_input.verb == "upload":

            if not parsed_input.obj or parsed_input.obj[0] == "csv":
                file_path_var = erql.upload_csv()
                df = pd.read_csv(file_path_var)
                file_info_text = (f"Filepath: {file_path_var} \n \n Columns: {df.columns.tolist()} \n \n")
                text_box.insert(tk.END, file_info_text)
                selected_file = fim.Filepath(file_path_var)


            elif parsed_input.obj[0] == "excel":
                error.show_warning("invalid_excel")

        elif parsed_input.verb == "convert":
            if len(parsed_input.obj) >= 2 and parsed_input.obj[0] == "excel" and parsed_input.obj[1] == "csv":
                df = pd.read_excel(erql.upload_excel())
                df.to_csv("file.csv", index=False)
            
            else:
                error.show_warning("missing_feature")


        elif parsed_input.verb == "info":
            csv_info = erql.file_info()
            text_box.insert(tk.END, csv_info)

    elif parsed_input.subject == "virtual_class":

        if parsed_input.verb == "info":
            df = erql.virtual_analyse()
            text_box.insert(tk.END, df)   

        elif parsed_input.verb == "graph":
            df = erql.virtual_analyse()
            fig = Figure()
            ax = fig.add_subplot(111)
            sns.barplot(x="Total", y="Nume Tutore", data=df, ax=ax)
            chart = FigureCanvasTkAgg(fig, master=canvas1)
            chart.draw()
            chart.get_tk_widget().pack(fill="both", expand=True)

    elif parsed_input.subject == "clear":
        text_box.delete("1.0", 'end')
        for widget in canvas1.winfo_children():
            widget.destroy()
    
    elif parsed_input.subject == "graph":
        for widget in canvas1.winfo_children():
            widget.destroy()
        if parsed_input.verb == "bar":
            sns.barplot(x=parsed_input.obj[0], y=parsed_input.obj[1], data=pd.read_csv(selected_file.filepath))
            plt.show()

        elif parsed_input.verb == "scatter":
            
            fig = Figure()
            ax = fig.add_subplot(111)
            sns.scatterplot(x=parsed_input.obj[0], y=parsed_input.obj[1], data=pd.read_csv(selected_file.filepath), ax=ax)
            plt.show()
            chart = FigureCanvasTkAgg(fig, master=canvas1)
            chart.draw()
            chart.get_tk_widget().pack(fill="both", expand=True)
            
    elif parsed_input.subject == "copy":
        text_box.tag_add(tk.SEL, "1.0", tk.END)
        text_box.clipboard_clear()
        text_box.clipboard_append(text_box.get("1.0", tk.END))



entry.bind('<Return>', enter)

btn = tk.Button(root, text="ENTER")
btn.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

root.mainloop()
