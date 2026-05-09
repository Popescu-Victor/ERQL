import math
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
from src import erql

def k_means(k_num, dataframe):
    df = dataframe
    k = k_num
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=k, random_state=0).fit(df)
    df['Cluster'] = kmeans.labels_

def hist(df):
    num_cols = df.select_dtypes(include='number').columns
    n = len(num_cols)
    ncols = 3
    nrows = math.ceil(n / ncols)

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(4*ncols, 2*nrows))
    axes = axes.flatten()

    for i, col in enumerate(num_cols):
        sns.kdeplot(df[col], fill=True, ax=axes[i])
        axes[i].axvline(df[col].median(), color='red', linestyle='--', linewidth=1.5, label=f'Median: {df[col].median():.2f}')
        axes[i].set_title(col,fontsize=10)
    for ax in axes.flatten():
        ax.set_ylabel('')
        ax.set_xlabel('')
    for j in range(i+1, len(axes)):
        axes[j].set_visible(False)
    plt.tight_layout(pad=2.0)
    return fig, ax

def correlation(df, target_col):
        other_cols = [col for col in df.select_dtypes(include='number').columns if col != target_col]

        n = len(other_cols)
        ncols = 3
        nrows = math.ceil(n / ncols)

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(4*ncols, 2*nrows))
        axes = axes.flatten()

        for i, col in enumerate(other_cols):
            sns.regplot(x=col, y=target_col, data=df, ax=axes[i], scatter_kws={'alpha':erql.set_alpha_level(df.shape[0]), "s":30} ,line_kws={"color":"red","linewidth":0.7, "linestyle":"--"})
            axes[i].set_title(f'{col} vs {target_col}')
            axes[i].set_xlabel("")
            axes[i].set_ylabel("")

        for j in range(i+1, len(axes)):
            axes[j].set_visible(False)

        plt.tight_layout()
        return fig, axes