from src import interpreter
from src import erql
import pandas as pd
from src import errors_messagebox as error

def command_handler(Parsed_input):
    if Parsed_input.subject == "standard":
        if Parsed_input.verb == "graph":
            if Parsed_input.obj[0] == "scatter":
                erql.scatter_plot(erql.df, erql.hor, erql.ver)

            elif Parsed_input.obj[0] == "bar":
                pass

            elif Parsed_input.obj[0] == "correlation":
                pass



    if Parsed_input.subject == "file":
        if Parsed_input.verb == "upload":
            if Parsed_input.obj == None:
                erql.upload_excel()
            if Parsed_input.obj[0] == "csv":
                erql.upload_csv()
    elif Parsed_input.subject == "homework":
        pass

    elif Parsed_input.subject == "group":
        pass
