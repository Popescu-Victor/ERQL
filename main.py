import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
import os
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
from utils import help
import math
from scraping import webdriver

root = tk.Tk()
# This is the main file of the program, where the GUI is created and the user input is processed.
# Creating the layout of the GUI using tkinter.
base_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_dir, "This2.ico")
root.iconbitmap(icon_path)

root.title("Education, Reporting & Query Language")
root.geometry("800x600")
root.columnconfigure(0, weight=8)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)

# The text box on the right is for displaying the output of the commands, while the canvas on the left is for displaying graphs and charts. The entry at the bottom is for the user to input their commands.
text_box = scrolledtext.ScrolledText(root,width=30,height=20,highlightthickness=2, highlightbackground="gray",wrap=tk.WORD)
text_box.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

canvas1 = tk.Frame(root,bg = "lightgray")
canvas1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

text_box2 = entry = tk.Entry(root, font=("Consolas", 16))
text_box2.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# This text gets pasted when the program starts so that first time users have some guidance on how to use the program. It also serves as a welcome message for returning users.
text_box.insert(tk.END, "Welcome to ERQL! If this is your first time using this app, write 'help>' in the field at the bottom left corner of the window.\n\n")

def enter(*args):
    global selected_file 
    global fig
    user_input = entry.get()
    parsed_input = interpreter.Parsed_input(user_input)
    if parsed_input.subject == "help":
        if parsed_input.verb =="":
            text_box.insert(tk.END, help_text)
        elif parsed_input.verb == "file":
            text_box.insert(tk.END, help.help_file)
        elif parsed_input.verb == "graph":
            text_box.insert(tk.END, help.help_graph)
        elif parsed_input.verb == "virtual_class":
            text_box.insert(tk.END, help.help_virtual_class)
        elif parsed_input.verb == "homework" or parsed_input.verb == "hw":
            text_box.insert(tk.END, help.help_homework)
        elif parsed_input.verb == "stats":
            text_box.insert(tk.END, help.help_stats)
        elif parsed_input.verb == "save":
            text_box.insert(tk.END, help.help_save)
    
    elif parsed_input.subject == "stats":
        for widget in canvas1.winfo_children():
            widget.destroy()
        df = pd.read_csv(selected_file.filepath)

        if parsed_input.verb == "kmeans":
            k = parsed_input.obj[0] if parsed_input.obj else 3
            erql.k_means(k, df)

        elif parsed_input.verb == "correlation":
            if not parsed_input.obj:
                error.show_warning("missing_arg_correlation")
                return
            else:
                target_col = parsed_input.obj[0]
                other_cols = [col for col in df.select_dtypes(include='number').columns if col != target_col]

                n = len(other_cols)
                ncols = 3
                nrows = math.ceil(n / ncols)

                fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(4*ncols, 2*nrows))
                axes = axes.flatten()

                for i, col in enumerate(other_cols):
                    sns.regplot(x=col, y=target_col, data=df, ax=axes[i], scatter_kws={'alpha':erql.set_alpha_level(df.shape[0]), "s":30} ,line_kws={"color":"red","linewidth":0.7, "linestyle":"--"})
                    axes[i].set_title(f'{col} vs {target_col}')
                    axes[i].set_xlabel("")
                    axes[i].set_ylabel("")

                for j in range(i+1, len(axes)):
                    axes[j].set_visible(False)

                plt.tight_layout()
                chart = FigureCanvasTkAgg(fig, master=canvas1)
                chart.draw()
                chart.get_tk_widget().pack(fill="both", expand=True)

        elif parsed_input.verb == "hist":
            num_cols = df.select_dtypes(include='number').columns
            n = len(num_cols)
            ncols = 3
            nrows = math.ceil(n / ncols)

            fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(4*ncols, 2*nrows))
            axes = axes.flatten()

            for i, col in enumerate(num_cols):
                sns.kdeplot(df[col], fill=True, ax=axes[i])
                axes[i].axvline(df[col].median(), color='red', linestyle='--', linewidth=1.5, label=f'Median: {df[col].median():.2f}')
                axes[i].set_title(col,fontsize=10)
            for ax in axes.flatten():
                ax.set_ylabel('')
                ax.set_xlabel('')
            for j in range(i+1, len(axes)):
                axes[j].set_visible(False)
            plt.tight_layout(pad=2.0)
            chart = FigureCanvasTkAgg(fig, master=canvas1)
            chart.draw()
            chart.get_tk_widget().pack(fill="both", expand=True)

            text = help.stats_hist(selected_file.filepath)
            text_box.insert(tk.END, text)
    


    elif parsed_input.subject == "file":

        if parsed_input.verb == "upload":

            if not parsed_input.obj or parsed_input.obj[0] == "csv":
                file_path_var = erql.upload_csv()
                df = pd.read_csv(file_path_var)
                file_name = file_path_var.split('/')[-1]
                file_info_text = (f"You have loaded: {file_name} into the program's memory. You can now perform actions on it. \n \nColumns: {df.columns.tolist()} \n \n")
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

        elif parsed_input.verb == "show":
            pass

        elif parsed_input.verb == "info":
            csv_info = erql.file_info()
            text_box.insert(tk.END, csv_info)

        elif parsed_input.verb == "anon":
            from utils import file_anonymizer_standard
            file_anonymizer_standard.file_anonymizer(parsed_input.obj[0])



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
            barplot = sns.barplot(x=parsed_input.obj[1], y=parsed_input.obj[0], data=pd.read_csv(selected_file.filepath))
            chart = FigureCanvasTkAgg(barplot.get_figure(), master=canvas1)
            chart.draw()
            chart.get_tk_widget().pack(fill="both", expand=True)

        elif parsed_input.verb == "scatter":
            df = pd.read_csv(selected_file.filepath)
            alpha_level = erql.set_alpha_level(df.shape[0])
            fig = Figure()
            ax = fig.add_subplot(111)
            sns.scatterplot(x=parsed_input.obj[0], y=parsed_input.obj[1], data=df, ax=ax, alpha=alpha_level)
            plt.show()
            chart = FigureCanvasTkAgg(fig, master=canvas1)
            chart.draw()
            chart.get_tk_widget().pack(fill="both", expand=True)

        elif parsed_input.verb == "correlation":
            fig = Figure()
            ax = fig.add_subplot(111)
            x = parsed_input.obj[0]
            y = parsed_input.obj[1]
            df = pd.read_csv(selected_file.filepath)
            print(df.shape[0])
            erql.correlation(df[x], df[y], ax, df.shape[0])
            chart = FigureCanvasTkAgg(fig, master=canvas1)
            chart.draw()
            chart.get_tk_widget().pack(fill="both", expand=True)

    elif parsed_input.subject == "copy":
        text_box.tag_add(tk.SEL, "1.0", tk.END)
        text_box.clipboard_clear()
        text_box.clipboard_append(text_box.get("1.0", tk.END))


# Saving graphs as image files and text as .txt files is also possible through the program. The user can choose where to save the file and what name to give it.

    elif parsed_input.subject == "save":
        if parsed_input.verb == "graph":
            save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")],
            title="Save Figure As")

            if save_path:
                fig.savefig(save_path)

        if parsed_input.verb == "text":
            save_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save Text As")

            if save_path:
                with open(save_path, 'w') as f:
                    f.write(text_box.get("1.0", tk.END))

    elif parsed_input.subject == "ilias":
        if parsed_input.verb == "login":
            global login
            login = erql.scrape_ilias(parsed_input.obj[0], parsed_input.obj[1])
            print(login)
        elif parsed_input.verb == "scrape":    
            webdriver.hw_scrape(login[0], login[1])

entry.bind('<Return>', enter)

btn = tk.Button(root, text="ENTER")
btn.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

root.mainloop()
