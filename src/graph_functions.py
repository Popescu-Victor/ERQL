import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from src import erql

def scatter(df, x_axis, y_axis, fig):
    alpha_level = erql.set_alpha_level(df.shape[0])
    ax = fig.add_subplot(111)
    sns.scatterplot(x=x_axis, y=y_axis, data=df, ax=ax, alpha=alpha_level)
    plt.show()