# Moved functions related to more complex statistical analysis into a different file.

def correlation():
            target_col = parsed_input.obj[0]
            other_cols = [col for col in df.select_dtypes(include='number').columns if col != target_col]

            n = len(other_cols)
            ncols = 3
            nrows = math.ceil(n / ncols)

            fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(4*ncols, 2*nrows))
            axes = axes.flatten()

            for i, col in enumerate(other_cols):
                sns.regplot(x=col, y=target_col, data=df, ax=axes[i], scatter_kws={'alpha':0.3, "s":30} ,line_kws={"color":"red","linewidth":0.7, "linestyle":"--"})
                axes[i].set_title(f'{col} vs {target_col}')

            for j in range(i+1, len(axes)):
                axes[j].set_visible(False)

            plt.tight_layout()
            chart = FigureCanvasTkAgg(fig, master=canvas1)
            chart.draw()
            chart.get_tk_widget().pack(fill="both", expand=True)


def knn():
  pass

def anova():
  pass

def lin_reg():
  pass

def log_reg():
  pass
