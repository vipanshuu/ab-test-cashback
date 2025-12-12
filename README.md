# A/B Testing Analysis – Cashback Offer

This project is a small A/B test analysis that I created to practice experiment evaluation using Python.  
I generated a synthetic dataset with two cashback variants:

- Variant A: 5% cashback  
- Variant B: ₹100 cashback (on transactions above ₹1000)

The goal was to compare conversion rates and check if the lift from Variant B is statistically significant.

### Key results from my run
- Conversion rate (A): 0.206  
- Conversion rate (B): 0.294  
- p-value from chi-square test: 0.000596  
This means Variant B performed better.

---

## Project Structure


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
