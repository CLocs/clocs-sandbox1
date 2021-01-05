import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv('./transactions_crop.csv')

# Convert date to date
df['Date']= pd.to_datetime(df['Date'])
# Set date as index cause its cool
df = df.set_index('Date')
print(type(df.index.values[0]))

# Slice on date (optional)
# df = df.loc[df.index.values[0] : df.index.values[3]]

# Group by the month of the date index (column probably works too)
# then Group by the category
# get the Amount column (cant sum the other columns, they are strings)
# sum the amounts for each category type
df = df.groupby([df.index.month, df.Category])["Amount"].sum()

print(df)
