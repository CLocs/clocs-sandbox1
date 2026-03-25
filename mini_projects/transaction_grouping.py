from pathlib import Path

import pandas as pd

# 1. Load your file (works for .xlsx or .csv)
filepath = r"E:\My Drive\Documents\Finances\Chase\Chase6830_Activity20250101_20251231_20260325.xlsx"
input_path = Path(filepath)
df = pd.read_excel(input_path)

# 2. Clean the merchant names (optional but helpful)
# This removes extra spaces or ensures everything is uppercase for better matching
df['Merchant'] = df['Description'].str.upper().str.strip()

# 3. Group by Merchant, count occurrences, and sum the amounts
summary = df.groupby('Merchant').agg(
    Count=('Amount', 'count'),
    Total_Spent=('Amount', 'sum')
).reset_index()

# 4. Filter for merchants that appear more than once (potential subscriptions)
# and sort by the most frequent first
subscriptions = summary[summary['Count'] > 1].sort_values(by='Count', ascending=False)

# 5. Save the results (same directory as the input file)
output_csv = input_path.parent / "transaction_grouping_results.csv"
subscriptions.to_csv(output_csv, index=False)
print(subscriptions.head(10))

