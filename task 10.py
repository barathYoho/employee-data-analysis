
import pandas as pd

# 1. Load CSV file
df = pd.read_csv("employees.csv")
print("Employee Data:")
print(df)

# 2. Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())
print("\nDataFrame Information:")
df.info()
print("\nStatistical Description:")
print(df.describe())

# 3. Select name column
print("\nEmployee Names:")
print(df["name"])
print("\nName and Salary:")
print(df[["name", "salary"]])

# 4. Using loc[] to get Chennai employees
print("\nChennai Employees:")
chennai = df.loc[df["city"] == "Chennai", "name"]
print(chennai.to_string(index=False))
print("\nUsing iloc:")
print(df.iloc[0:3, 1:3])

# 5. Filter employees with salary above 50000
high_salary = df[df["salary"] > 50000]
print("\nEmployees with salary above 50000:")
print(high_salary)
print("Salary above 50000:", len(high_salary), "employees")
it_employees = df[df["department"] == "IT"]
print("\nIT Department Employees:")
print(it_employees["name"].to_string(index=False))
print("IT department:", len(it_employees), "employees")
