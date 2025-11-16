"""
stats_tests.py - Statistical test functions for Walmart analysis.
"""

import numpy as np
from scipy import stats

def ttest_gender(male_values, female_values):
    """Two-sample independent t-test."""
    return stats.ttest_ind(male_values, female_values, equal_var=False)

def bootstrap_mean_ci(data, n_bootstrap=2000, ci=95):
    """Bootstrap confidence interval for mean."""
    means = []
    for _ in range(n_bootstrap):
        sample = np.random.choice(data, size=len(data), replace=True)
        means.append(np.mean(sample))
    lower = np.percentile(means, (100-ci)/2)
    upper = np.percentile(means, 100 - (100-ci)/2)
    return lower, upper
