import pandas as pd
import numpy as np
np.random.seed(42)
n_users = 1200
user_ids = np.arange(1, n_users+1)
groups = np.random.choice(['A','B'], size=n_users)
shown_offer = np.ones(n_users, dtype=int)
clicked_offer = np.random.binomial(1, 0.40, size=n_users)
made_transaction = []
transaction_amount = []
for g in groups:
    if g == 'A':
        conv = np.random.rand() < 0.20
    else:
        conv = np.random.rand() < 0.27
    made_transaction.append(int(conv))
    transaction_amount.append(np.random.randint(300, 3001) if conv else 0)
signup_dates = pd.to_datetime('2025-01-01') + pd.to_timedelta(np.random.randint(0,180,size=n_users), unit='D')
device_type = np.random.choice(['Android','iOS'], size=n_users, p=[0.6,0.4])
df = pd.DataFrame({
    "user_id": user_ids,
    "group": groups,
    "shown_offer": shown_offer,
    "clicked_offer": clicked_offer,
    "made_transaction": made_transaction,
    "transaction_amount": transaction_amount,
    "signup_date": signup_dates.date,
    "device_type": device_type
})
df.to_csv("data/ab_test_cashback.csv", index=False)
print("Saved data/ab_test_cashback.csv")
