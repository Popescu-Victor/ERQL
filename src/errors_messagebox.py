from tkinter import messagebox

WARNINGS = {
    "args_number":      ("Error: args_number",    "Your input has the wrong number of arguments."),
    "invalid_syntax":   ("Error: invalid_syntax",  "Please separate your arguments using the '>' sign with no spaces"),
    "invalid_subject":  ("Error: invalid_subject", "Invalid first argument. Use 'help>subjects' for more information."),
    "invalid_verb": ("Error: invalid_verb", "Invalid second argument. Use 'help>verbs' for more information."),
    "wrong_file_type": ("Error: wrong_file_type", "Please use files with the .csv extension"),
    "no_file": ("Error: no_file", "Please first upload a file using 'standard>upload' before performin analysis"),
    "invalid_data_type": ("Error: invalid_data_type", "Invalid data found in input. Please make sure the columns you're selecting are correctly formatted."),
    "title_error": ("Error: title_error", "ERQL can only perform this operation on files scraped from 'roarmy'."),
    "missing_feature": ("Error: missing_feature", "The feature you are trying to access has not been implemented yet."),
    "invalid_excel": ("Error: invalid_excel", "ERQL can't currently handle excel files. Please convert your files to .csv before use.")
                        
}

def show_warning(key):
    title, message = WARNINGS[key]
    messagebox.showwarning(title, message)
    
