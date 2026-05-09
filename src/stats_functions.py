import math
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

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
