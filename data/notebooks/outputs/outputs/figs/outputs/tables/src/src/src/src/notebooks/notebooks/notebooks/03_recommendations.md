# 03 - Business Insights, Recommendations & Experiment Design

**Goal:** Transform statistical findings into actionable business strategies and design an A/B test for validation.

---

# 1. Summary of Statistical Findings

### ✔ Gender Spending Difference (Significant)
- Male average purchase > Female average purchase  
- t-test p-value ≈ 0 → **difference is statistically significant**  
- Cohen’s d (effect size) → medium impact range  
- Bootstrap CIs do NOT overlap → strong separation  

### ✔ Marital Status (Not Significant)
- Means very close  
- Confidence intervals overlap heavily  
- No purchasing difference worth acting on  

### ✔ Age Groups (Weak Trend)
- Spending increases slightly with age  
- But overlapping CIs → **not strong enough** for segmentation  

---

# 2. Visual Summary (importing figures generated in earlier notebooks)

```python
from IPython.display import Image, display

# gender boxplot
display(Image("../outputs/figs/purchase_by_gender.png"))

# mean CI plot
display(Image("../outputs/figs/gender_mean_ci.png"))
