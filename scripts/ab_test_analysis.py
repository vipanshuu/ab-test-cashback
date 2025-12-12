import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.makedirs("outputs/plots", exist_ok=True)
df = pd.read_csv("data/ab_test_cashback.csv")
grp = df.groupby("group").agg(
    users=("user_id","nunique"),
    shown=("shown_offer","sum"),
    clicks=("clicked_offer","sum"),
    conversions=("made_transaction","sum"),
    total_revenue=("transaction_amount","sum")
).reset_index()
grp["ctr"] = grp["clicks"] / grp["shown"]
grp["conversion_rate"] = grp["conversions"] / grp["shown"]
grp["avg_transaction_amount"] = grp["total_revenue"] / grp["conversions"].replace(0, np.nan)
grp.to_csv("outputs/ab_test_summary_by_group.csv", index=False)
cont = pd.crosstab(df["group"], df["made_transaction"])
cont.to_csv("outputs/ab_test_contingency.csv")
chi2, p, dof, expected = chi2_contingency(cont)
sns.set(style="whitegrid")
plt.figure(figsize=(6,4))
sns.barplot(x="group", y="conversion_rate", data=grp)
plt.title("Conversion Rate by Group")
plt.ylabel("Conversion Rate")
plt.ylim(0, grp["conversion_rate"].max() * 1.4)
plt.savefig("outputs/plots/conversion_by_group.png", bbox_inches="tight")
plt.close()
paid = df[df["transaction_amount"]>0]
plt.figure(figsize=(6,4))
sns.boxplot(x="group", y="transaction_amount", data=paid)
plt.title("Transaction Amount Distribution (converted users)")
plt.ylabel("Transaction Amount (₹)")
plt.savefig("outputs/plots/revenue_by_group.png", bbox_inches="tight")
plt.close()
a_conv = grp.loc[grp["group"]=="A","conversion_rate"].values[0]
b_conv = grp.loc[grp["group"]=="B","conversion_rate"].values[0]
print(f"Conversion A: {a_conv:.3f}, Conversion B: {b_conv:.3f}, p-value: {p:.6f}")
