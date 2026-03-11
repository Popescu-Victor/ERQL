import erql
import pandas as pd
from interpreter import Render
import matplotlib.pyplot as plt



input_user = input("Now what? \n")
rendered = Render(input_user)



if rendered.subj == "standard":
    if rendered.verb == "plot":
        erql.scatter_plot(rendered.mod[0], rendered.mod[1])
        
    if rendered.verb == "upload":
        uploaded_file = erql.upload()
        print(uploaded_file.file.head())
