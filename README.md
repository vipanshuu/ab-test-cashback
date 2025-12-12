# A/B Testing Analysis — Cashback Offer (Fintech)

Summary
Analyzed a simulated A/B experiment comparing two cashback variants:
- Variant A: 5% cashback
- Variant B: ₹100 cashback for transactions > ₹1000

Key Results (from the synthetic run)
- Conversion rate: A = 0.206, B = 0.294
- Chi-square p-value: 0.000596
Business recommendation: Roll out Variant B (higher conversion).

Files
data/ab_test_cashback.csv
scripts/generate_data.py
scripts/ab_test_analysis.py
outputs/ab_test_summary_by_group.csv
outputs/ab_test_contingency.csv
outputs/plots/conversion_by_group.png
outputs/plots/revenue_by_group.png

How to run
pip install pandas scipy matplotlib seaborn
python scripts/generate_data.py
python scripts/ab_test_analysis.py

Contact
Vipanshu Sharma — info.vipanshu@gmail.com
