# 01 - Exploration (Walmart Black Friday)

**Goal:** load data, check structure, clean minimal issues, compute summary stats and save initial outputs.

---

## 1. Imports & settings
```python
# cell: imports
import os
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# display settings
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 120)

# cell: load data (update filepath if needed)
DATA_PATH = "../data/walmart_blackfriday.csv"   # put the real CSV path here or adjust
df = pd.read_csv(DATA_PATH)
df.shape, df.head(3)

# cell: info & missing
df.info()
df.isnull().sum()

# cell: quick cleaning placeholders
# - drop exact duplicates
df = df.drop_duplicates()
# - if there are cancellation or invalid flags, filter (adjust column names)
# df = df[df['Status'] != 'Cancelled']   # uncomment and edit if relevant

# show shape after cleaning
df.shape

# cell: summary stats
overall_mean = df['Purchase'].mean()
overall_median = df['Purchase'].median()
overall_mean, overall_median

# by gender
gender_stats = df.groupby('Gender')['Purchase'].agg(['count','mean','median','std']).reset_index()
gender_stats

# cell: save summary
os.makedirs('../outputs/tables', exist_ok=True)
gender_stats.to_csv('../outputs/tables/gender_summary.csv', index=False)

# cell: boxplot
os.makedirs('../outputs/figs', exist_ok=True)
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x='Gender', y='Purchase')
plt.title('Purchase by Gender')
plt.savefig('../outputs/figs/purchase_by_gender.png', bbox_inches='tight')
plt.show()
