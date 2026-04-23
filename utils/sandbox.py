import pandas as pd
import plotly.figure_factory as ff


file = r"C:\Users\popescu.victor\Desktop\NCA\table.csv"
df = pd.read_csv(file)

fig = ff.create_table(df)
fig.show()
