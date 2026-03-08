import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Layout Example")
root.geometry("600x400")

root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=2)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

canvas = tk.Canvas(root, bg="lightgray")
canvas.grid(row=0, column=0, sticky="nsew")

scroll_text = scrolledtext.ScrolledText(root)
scroll_text.grid(row=0, column=1, sticky="nsew")

entry = tk.Entry(root)
entry.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

btn1 = tk.Button(root, text="Button")
btn1.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

text = tk.Text(root, height=5)
text.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

btn2 = tk.Button(root, text="Button")
btn2.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

root.mainloop()
