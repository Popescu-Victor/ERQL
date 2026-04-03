from src import interpreter
from src import erql
import pandas as pd
import errors_messagebox as error

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
            error.show_warning("missing_feature")
    elif Parsed_input.subject == "homework":
        pass

    elif Parsed_input.subject == "group":
        pass
