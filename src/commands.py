import interpreter
import erql
import pandas as pd

def command_handler(Parsed_input):
    if Parsed_input.subject == "standard":
        if Parsed_input.verb == "graph":
            if Parsed_input.obj[0] == "scatter":
                erql.scatter_plot(erql.df, erql.hor, erql.ver)
                
    if Parsed_input.subject == "file":

    if Parsed_input.subject == "homework":

    if Parsed_input.subject == "group":
