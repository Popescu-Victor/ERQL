import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from src import interpreter
from src import commands
from src import erql
from pathlib import Path
import pandas as pd
import openpyxl
import seaborn as sns
from src import errors_messagebox as error
from src import stats_functions as st
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

graph_area_canvas = tk.Frame(root,bg = "lightgray")
graph_area_canvas.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

text_box2 = entry = tk.Entry(root, font=("Consolas", 16))
text_box2.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# This text gets pasted when the program starts so that first time users have some guidance on how to use the program. It also serves as a welcome message for returning users.
text_box.insert(tk.END, "Welcome to ERQL! If this is your first time using this app, write 'help>' in the field at the bottom left corner of the window.\n\n")

def press_enter(*args):
    global selected_file 
    global fig
    user_input = entry.get()
    parsed_input = interpreter.Parsed_input(user_input)
    if parsed_input.subject == "help":
        # The help command is for providing guidance on how to use the program. If the user writes "help>" they get a general help text, but if they write "help>file" for example, they get help related to file commands.
    
        if parsed_input.verb =="":
            text_box.insert(tk.END, help_text)
        elif parsed_input.verb=="groups":
            text_box.insert(tk.END, help.help_groups)
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
    
    elif parsed_input.subject == "stats": # Statistical analysis, usually done on multiple columns at once or even to the entire dataset where possible.
        for widget in graph_area_canvas.winfo_children():
            widget.destroy()
        df = pd.read_csv(selected_file.filepath)

        if parsed_input.verb == "kmeans":
            k = parsed_input.obj[0] if parsed_input.obj else 3 # Default to 3 clusters if not specified
            st.k_means(k, df)

        elif parsed_input.verb == "correlation":
            if not parsed_input.obj:
                error.show_warning("missing_arg_correlation")
                return
            else:
                fig_ax = st.correlation(df=df, target_col=parsed_input.obj[0])
                fig = fig_ax[0]
                chart = FigureCanvasTkAgg(fig, master=graph_area_canvas)
                chart.draw()
                chart.get_tk_widget().pack(fill="both", expand=True)

        elif parsed_input.verb == "hist": # Histogram, shows distribution of data in all numberical columns of the dataset.
            fig_ax = st.hist(df)
            fig = fig_ax[0]
            chart = FigureCanvasTkAgg(fig, master=graph_area_canvas)
            chart.draw()
            chart.get_tk_widget().pack(fill="both", expand=True)

            text = help.stats_hist(selected_file.filepath)
            text_box.insert(tk.END, text)
    


    elif parsed_input.subject == "file": # Actions related to files (.csv) on your computer.

        if parsed_input.verb == "upload": # This is for loading a .csv file's path into the program's memory for further reference and actions.

            if not parsed_input.obj or parsed_input.obj[0] == "csv":
                file_path_var = erql.upload_csv()
                df = pd.read_csv(file_path_var)
                file_name = file_path_var.split('/')[-1]
                file_info_text = (f"You have loaded: {file_name} into the program's memory. You can now perform actions on it. \n \nColumns: {df.columns.tolist()} \n \n")
                text_box.insert(tk.END, file_info_text)
                selected_file = fim.Filepath(file_path_var)


            elif parsed_input.obj[0] == "excel":
                error.show_warning("invalid_excel") # Haven't yet implemented excel access.

        elif parsed_input.verb == "convert":
            if len(parsed_input.obj) >= 2 and parsed_input.obj[0] == "excel" and parsed_input.obj[1] == "csv":
                df = pd.read_excel(erql.upload_excel())
                df.to_csv("file.csv", index=False)
            
            else:
                error.show_warning("missing_feature")

        elif parsed_input.verb == "show":
            pass

        elif parsed_input.verb == "info": # Prints information about loaded file.
            csv_info = erql.file_info()
            text_box.insert(tk.END, csv_info)

        elif parsed_input.verb == "anon": # For data complience reasons, you might want to randomize file names (for example if the files contain people's name or other forms of PII). When running file>anon>filepath, every file in a chose folder will get randomly generated names.
            from utils import file_anonymizer_standard
            swaps = file_anonymizer_standard.file_anonymizer(parsed_input.obj[0])
            result = ", ".join(swaps)
            text_box.insert(tk.END, result)

    elif parsed_input.subject == "groups": # Related to grouping students under teachers or tutors for organizational purposes. You can also print out information about the groups you have created and the students in them.
        import sqlite3
        conn = sqlite3.connect('groups.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS groups(teacher TEXT, student TEXT);')
        if parsed_input.verb and parsed_input.obj:
            teacher_student = [parsed_input.verb, parsed_input.obj[0]]
            cursor.execute("INSERT INTO groups VALUES (?,?);", teacher_student)
            conn.commit()
            conn.close()
            text_insert = f'Added {parsed_input.obj[0]} as a student of {parsed_input.verb} \n'
            text_box.insert(tk.END, text_insert)
        else:
            error.show_warning('args_number')

    elif parsed_input.subject == "virtual_class": # Also related to specific kinds of graphs and analyses that are relevant for teachers and tutors

        if parsed_input.verb == "info":
            df = erql.virtual_analyse()
            text_box.insert(tk.END, df)   

        elif parsed_input.verb == "graph":
            df = erql.virtual_analyse()
            fig = Figure()
            ax = fig.add_subplot(111)
            sns.barplot(x="Total", y="Nume Tutore", data=df, ax=ax)
            chart = FigureCanvasTkAgg(fig, master=graph_area_canvas)
            chart.draw()
            chart.get_tk_widget().pack(fill="both", expand=True)

    elif parsed_input.subject == "clear": # Clears out graph and text areas.
        text_box.delete("1.0", 'end')
        for widget in graph_area_canvas.winfo_children():
            widget.destroy()
    
    elif parsed_input.subject == "graph": # For creating graphs and charts.
        for widget in graph_area_canvas.winfo_children():
            widget.destroy()
        if not parsed_input.obj or len(parsed_input.obj) < 2 or not parsed_input.obj[1]:
                error.show_warning('args_number')
        else:

            if parsed_input.verb == "bar":
                if not parsed_input.obj or len(parsed_input.obj) < 2 or not parsed_input.obj[1]:
                    error.show_warning('args_number')
                else:
                    barplot = sns.barplot(x=parsed_input.obj[1], y=parsed_input.obj[0], data=pd.read_csv(selected_file.filepath))
                    chart = FigureCanvasTkAgg(barplot.get_figure(), master=graph_area_canvas)
                    chart.draw()
                    chart.get_tk_widget().pack(fill="both", expand=True)

            elif parsed_input.verb == "scatter": # To create a scatter plot you run graph>file>x_axis>y_axis. Chose the X and Y axes using the information printed out in the text area when uploading a file using file>upload.
                
                df = pd.read_csv(selected_file.filepath)
                alpha_level = erql.set_alpha_level(df.shape[0])
                fig = Figure()
                ax = fig.add_subplot(111)
                sns.scatterplot(x=parsed_input.obj[0], y=parsed_input.obj[1], data=df, ax=ax, alpha=alpha_level)
                plt.show()
                chart = FigureCanvasTkAgg(fig, master=graph_area_canvas)
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
                chart = FigureCanvasTkAgg(fig, master=graph_area_canvas)
                chart.draw()
                chart.get_tk_widget().pack(fill="both", expand=True)

    elif parsed_input.subject == "copy": # Same as selecting all the text in the text area and hitting CTRL+C
        text_box.tag_add(tk.SEL, "1.0", tk.END)
        text_box.clipboard_clear()
        text_box.clipboard_append(text_box.get("1.0", tk.END))

    elif parsed_input.subject == "cloud":
        from tkinter import filedialog # For security reasons, the program doesn't ask you to write the credentials for your cloud services in the command line, but instead opens a file explorer window where you can select the credentials file from your computer. This way, the credentials don't get stored in the program's memory or in the command history.
        cred_file = filedialog.askopenfilename(title="Select a file", filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
        print(cred_file)

    elif parsed_input.subject == "telegram":
        from telegram_bot import telegram_bot
        if parsed_input.verb == "start":
            user_message = telegram_bot.start_telegram_bot()
            text_box.insert(tk.END, user_message)





# Saving graphs as image files and text as .txt files is also possible through the program. The user can choose where to save the file and what name to give it.

    elif parsed_input.subject == "save":
        from tkinter import filedialog
        if parsed_input.verb == "graph": # After creating a graph inside the ERQL program, you can save it as an image file on your computer by running save>graph. You can choose where to save it and what name to give it.
            save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")],
            title="Save Figure As")

            if save_path:
                fig.savefig(save_path)

        if parsed_input.verb == "text": # Saving the text from the textbox on the right.
            save_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save Text As")

            if save_path:
                with open(save_path, 'w') as f:
                    f.write(text_box.get("1.0", tk.END))

    elif parsed_input.subject == "ilias": # Actions related to the ILIAS LMS. 

        if parsed_input.verb == "scrape":    
            hw_list = webdriver.hw_scrape(parsed_input.obj[0], parsed_input.obj[1])
            text_box.insert(tk.END, "Here are the homework links I found: \n")
            for hw in hw_list:
                text_box.insert(tk.END, hw + "\n")

entry.bind('<Return>', press_enter)

btn = tk.Button(root, text="ENTER")
btn.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

root.mainloop()