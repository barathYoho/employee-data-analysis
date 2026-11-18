
import pandas as pd

# 1. Load CSV file
df = pd.read_csv("orders.csv")
print("Original Data:")
print(df)

# 2. Find missing values
print("\nMissing Values:")
print(df.isna().sum())
print("\nDuplicate Rows:")
print(df.duplicated())
missing = df["amount"].isna().sum()
duplicates = df.duplicated().sum()
print("\nMissing: amount", missing, "| Duplicates:", duplicates)

# 3. Remove duplicate rows
df = df.drop_duplicates()
median_value = df["amount"].median()
print("\nMedian used:", median_value)
df["amount"] = df["amount"].fillna(median_value)

# 4. Convert data types
df["amount"] = pd.to_numeric(df["amount"])
df["order_id"] = df["order_id"].astype(str)
print("\nCleaned Data:")
print(df)

# 5. Group by customer_id and aggregate
result = df.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)
print("\nCustomer Order Summary:")
print(result)
