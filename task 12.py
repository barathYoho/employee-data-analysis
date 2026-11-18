
import pandas as pd

# 1. Load orders and customers CSV files
orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")

# 2. Clean orders dataset
orders = orders.drop_duplicates()
median_value = orders["amount"].median()
orders["amount"] = orders["amount"].fillna(median_value)
orders["order_id"] = orders["order_id"].astype(str)
orders["amount"] = pd.to_numeric(orders["amount"])

# 3. Inner Join
inner = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="inner"
)
print("INNER JOIN:")
print(inner)
print("Inner join rows:", len(inner))

# 4. Left Join
left = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="left",
    indicator=True
)
print("\nLEFT JOIN:")
print(left)
no_orders = left[left["_merge"] == "left_only"]
print("\nCustomers with no orders:")
print(no_orders["name"].to_string(index=False))

# 5. Outer Join
outer = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="outer",
    indicator=True
)
print("\nOUTER JOIN:")
print(outer)
unmatched = outer[outer["_merge"] == "left_only"]
print("\nOrder without customer:")
print(unmatched[["customer_id"]])
