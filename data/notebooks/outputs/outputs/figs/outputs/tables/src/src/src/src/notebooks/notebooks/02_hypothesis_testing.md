# 02 - Hypothesis testing (Gender & effect size)

**Goal:** run two-sample t-test for gender, compute Cohen's d, and get bootstrap CIs for group means.

---

## 1. Imports & settings
```python
# cell: imports
import os
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 50)

# cell: load data
DATA_PATH = "../data/walmart_blackfriday.csv"  # update if you placed cleaned CSV somewhere else
df = pd.read_csv(DATA_PATH)
df.shape

# cell: extract groups
# ensure gender column name matches your dataset ('Gender' is expected)
df = df.dropna(subset=['Gender','Purchase'])  # drop rows missing essential columns
male_vals = df.loc[df['Gender']=='M', 'Purchase'].values
female_vals = df.loc[df['Gender']=='F', 'Purchase'].values

len(male_vals), len(female_vals)

# cell: t-test
tt_res = stats.ttest_ind(male_vals, female_vals, equal_var=False)
print("t-statistic:", tt_res.statistic)
print("p-value:", tt_res.pvalue)

# cell: cohen's d
def cohens_d(x, y):
    nx = len(x); ny = len(y)
    dof = nx + ny - 2
    pooled_std = np.sqrt(((nx-1)*np.var(x, ddof=1) + (ny-1)*np.var(y, ddof=1)) / dof)
    return (np.mean(x) - np.mean(y)) / pooled_std

d = cohens_d(male_vals, female_vals)
d

# cell: bootstrap CI
def bootstrap_mean_ci(data, n_bootstrap=2000, ci=95, seed=42):
    rng = np.random.default_rng(seed)
    means = []
    for _ in range(n_bootstrap):
        sample = rng.choice(data, size=len(data), replace=True)
        means.append(sample.mean())
    lower = np.percentile(means, (100-ci)/2)
    upper = np.percentile(means, 100 - (100-ci)/2)
    return lower, upper

m_lower, m_upper = bootstrap_mean_ci(male_vals, n_bootstrap=2000)
f_lower, f_upper = bootstrap_mean_ci(female_vals, n_bootstrap=2000)

print("Male mean CI:", m_lower, m_upper)
print("Female mean CI:", f_lower, f_upper)

# cell: save summary results
os.makedirs('../outputs/tables', exist_ok=True)
summary = {
    'group':['male','female'],
    'count':[len(male_vals), len(female_vals)],
    'mean':[np.mean(male_vals), np.mean(female_vals)],
    'std':[np.std(male_vals, ddof=1), np.std(female_vals, ddof=1)],
    'ci_lower':[m_lower, f_lower],
    'ci_upper':[m_upper, f_upper]
}
summary_df = pd.DataFrame(summary)
summary_df.to_csv('../outputs/tables/gender_test_summary.csv', index=False)

# save a quick text report
with open('../outputs/tables/gender_test_report.txt','w') as f:
    f.write(f"t-statistic: {tt_res.statistic}\n")
    f.write(f"p-value: {tt_res.pvalue}\n")
    f.write(f"cohens_d: {d}\n")

# cell: mean with errorbars
os.makedirs('../outputs/figs', exist_ok=True)
means = [np.mean(male_vals), np.mean(female_vals)]
errs = [np.mean(male_vals)-m_lower, np.mean(female_vals)-f_lower]

plt.figure(figsize=(5,4))
plt.bar(['Male','Female'], means, yerr=errs, capsize=8)
plt.ylabel('Average Purchase')
plt.title('Group means with bootstrap 95% CI')
plt.savefig('../outputs/figs/gender_mean_ci.png', bbox_inches='tight')
plt.show()

