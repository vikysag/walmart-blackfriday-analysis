"""
viz.py - Visualization helper functions.
"""

import matplotlib.pyplot as plt
import seaborn as sns

def boxplot_by_group(df, x, y, title):
    plt.figure(figsize=(8,5))
    sns.boxplot(data=df, x=x, y=y)
    plt.title(title)
    plt.show()
