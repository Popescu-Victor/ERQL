import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv(r"C:\Users\popescu.victor\Desktop\NCA\churn.csv")

col_index = 4
col_name = df.columns[col_index]


n_rows = len(df)
n_cols = 4  
n_grid_rows = math.ceil(n_rows / n_cols)

fig, axs = plt.subplots(n_grid_rows, n_cols, figsize=(4*n_cols, 4*n_grid_rows))
axs = axs.flatten() 

for i, ax in enumerate(axs):
    if i < n_rows:
        value = df.iloc[i, col_index]
        name = df.iloc[i, 0]  


        ax.pie([value, 100 - value], labels=[col_name, ""], autopct='%1.1f%%', startangle=90)
        ax.set_title(name)
    else:
        ax.axis("off")  

plt.tight_layout()
plt.show()
