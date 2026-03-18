from tkinter import messagebox

WARNINGS = {
    "args_number":      ("Error: args_number",    "Your input has the wrong number of arguments."),
    "invalid_syntax":   ("Error: invalid_syntax",  "Please separate your arguments using the '>' sign with no spaces"),
    "invalid_subject":  ("Error: invalid_subject", "Invalid first argument. Use 'help>subjects' for more information."),
    "invalid_verb": ("Error: invalid_verb", "Invalid second argument. Use 'help>verbs' for more information."),
    "wrong_file_type": ("Error: wrong_file_type", "Please use files with the .csv extension"),
    "no_file": ("Error: no_file", "Please first upload a file using 'standard>upload' before performin analysis")



}

def show_warning(key):
    title, message = WARNINGS[key]
    messagebox.showwarning(title, message)
    
show_warning("args_number")
