**Walmart Black Friday Purchase Behavior Analysis**

Data Size: 550,068 transactions | Tech: Python, Pandas, NumPy, SciPy, Matplotlib

**📌 Project Overview**

This project analyzes customer purchase behavior during Walmart's Black Friday sales using exploratory data analysis and statistical hypothesis testing. The goal is to understand how gender, marital status, and age groups influence purchase amounts and derive business insights.

**🔍 Key Business Questions**

Do male and female customers spend differently?

Does marital status impact purchase amount?

Do age groups show meaningful differences?

**📊 Techniques Used**

**Descriptive statistics**

Data visualization (boxplots, histograms, KDE)

Two-sample t-test

Bootstrap Confidence Intervals

Central Limit Theorem (CLT) sampling


📈 **Key Findings**
1.  **Gender-Based Spending **(Statistically Significant)

Male average purchase: ₹9,437.53

Female average purchase: ₹8,734.57

Two-sample t-test: p-value ≈ 0 → difference is statistically significant
➡️ Male customers spend more per transaction than female customers.

2.  **Marital Status** (Not Significant)

Mean purchase amounts across marital-status groups show only small differences.

Confidence intervals overlap.
➡️ No meaningful effect of marital status on purchase amount.

3.  **Age Groups** (Weak Trend)

Purchase amount tends to increase slightly with age.

But confidence intervals heavily overlap.
➡️ Age has a mild upward trend but is not strong enough to be statistically conclusive.


## 📂 Project Structure  
...

git clone https://github.com/vikysag/walmart-blackfriday-analysis.git
cd walmart-blackfriday-analysis


pip install pandas numpy scipy matplotlib seaborn
