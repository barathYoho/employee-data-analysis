
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("reports/figures", exist_ok=True)


print("\n========== NUMPY ANALYSIS ==========")

marks = np.array([
    [80, 75, 90],
    [65, 70, 85],
    [90, 88, 95],
    [72, 80, 78]
])

print("Marks Array:\n", marks)
print("Array Shape:", marks.shape)

student_averages = np.mean(marks, axis=1)
print("Student averages:", student_averages)

subject_averages = np.mean(marks, axis=0)
print("Subject averages:", subject_averages)

grace_marks = marks + 5
print("Marks after adding 5 grace marks:\n", grace_marks)

weights = np.array([0.2, 0.3, 0.5])
weighted_scores = np.dot(grace_marks, weights)
print("Weighted scores:", weighted_scores)



print("\n========== PANDAS ANALYSIS ==========")

df = pd.read_csv("employees.csv")

print("\nDataFrame Information:")
df.info()

print("\nDescriptive Statistics:")
print(df.describe())

print("\nUsing loc:")
print(df.loc[0])

print("\nUsing iloc:")
print(df.iloc[0])

print("\nEmployees with salary above 50000:")
print(df[df["salary"] > 50000])

dirty_df = df.copy()


dirty_df.loc[dirty_df["id"] == 1, "salary"] = np.nan
dirty_df.loc[dirty_df["id"] == 2, "salary"] = np.nan


dirty_df = pd.concat(
    [dirty_df, dirty_df.iloc[[2]]],
    ignore_index=True
)

dirty_df.to_csv("employees_dirty.csv", index=False)

print("\nDirty dataset created:")
print("Rows before cleaning:", len(dirty_df))
print("Missing salaries:", dirty_df["salary"].isna().sum())
print("Duplicate rows:", dirty_df.duplicated().sum())



dirty_df["id"] = pd.to_numeric(
    dirty_df["id"], errors="coerce"
).astype("Int64")

dirty_df["salary"] = pd.to_numeric(
    dirty_df["salary"], errors="coerce"
)


median_salary = dirty_df["salary"].median()
dirty_df["salary"] = dirty_df["salary"].fillna(median_salary)


clean_df = dirty_df.drop_duplicates().copy()


clean_df["id"] = clean_df["id"].astype(int)
clean_df["salary"] = clean_df["salary"].astype(float)

print("\nCleaned Dataset:")
print(clean_df)

print("\nMissing values after cleaning:")
print(clean_df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(clean_df.duplicated().sum())

print("\nRows after cleaning:", len(clean_df))

print("\n========== DEPARTMENT ANALYSIS ==========")

department_summary = clean_df.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
).reset_index()

print("\nDepartment Summary:")
print(department_summary)

print("\nHeadcount:")
for _, row in department_summary.iterrows():
    print(f'{row["department"]}: {row["headcount"]}')



departments = pd.read_csv("departments.csv")

print("\nDepartments Data:")
print(departments)


inner_join = pd.merge(
    department_summary,
    departments,
    on="department",
    how="inner"
)

print("\nINNER JOIN:")
print(inner_join)


left_join = pd.merge(
    departments,
    department_summary,
    on="department",
    how="left"
)

print("\nLEFT JOIN:")
print(left_join)

outer_join = pd.merge(
    departments,
    department_summary,
    on="department",
    how="outer"
)

print("\nOUTER JOIN:")
print(outer_join)

# Find departments without employees
no_employees = outer_join[
    outer_join["headcount"].isna()
]["department"].tolist()

print("\nDepartments with no employees:", no_employees)

plt.figure(figsize=(8, 5))

plt.bar(
    department_summary["department"],
    department_summary["average_salary"],
    label="Average Salary"
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()

plt.savefig("reports/figures/bar_chart.png")
plt.close()

print("\nBar Chart Insight: Finance has the highest average salary at 90000, while HR has the lowest at 54000.")



plt.figure(figsize=(8, 5))

plt.hist(
    clean_df["salary"],
    bins=5,
    edgecolor="black",
    label="Employee Salary"
)

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()

plt.savefig("reports/figures/histogram.png")
plt.close()

print("Histogram Insight: The histogram shows how employee salaries are distributed across salary ranges.")

plt.figure(figsize=(8, 5))

plt.scatter(
    clean_df["id"],
    clean_df["salary"],
    label="Employee Salary"
)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()

plt.savefig("reports/figures/scatter_plot.png")
plt.close()

print("Scatter Insight: The scatter plot compares individual employee salaries by employee ID.")


plt.figure(figsize=(8, 5))

plt.plot(
    clean_df["id"],
    clean_df["salary"],
    marker="o",
    label="Employee Salary"
)

plt.title("Employee Salary Trend")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()

plt.savefig("reports/figures/line_chart.png")
plt.close()

print("Line Chart Insight: The line chart shows how salaries vary across employee IDs.")
print("4. reports/figures/line_chart.png")


print("\n========== TASK 3 COMPLETED ==========")
print("Generated files:")
print("1. employees_dirty.csv")
print("2. reports/figures/bar_chart.png")
print("3. reports/figures/histogram.png")
print("4. reports/figures/scatter_plot.png")
print("5. reports/figures/line_chart.png")
