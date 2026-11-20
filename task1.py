
import csv



# 1. FUNCTION USING *args AND **kwargs
def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result


# 2. CUSTOM EXCEPTION
class InvalidSalaryError(Exception):
    pass


# 3. EMPLOYEE CLASS
class Employee:

    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


# 4. MANAGER CLASS (INHERITANCE)
class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Manager: {self.name}, "
            f"Salary: {self.salary}, "
            f"Team Size: {self.team_size}"
        )


# 5. READ EMPLOYEE DATA FROM CSV
with open("employees.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    print("CSV Columns:", reader.fieldnames)

    employees = list(reader)

for emp in employees:
    emp["salary"] = int(emp["salary"])


# 6. LIST COMPREHENSION
above_50000 = [
    emp["name"]
    for emp in employees
    if emp["salary"] > 50000
]

print("Above 50000:", above_50000)


# 7. MAP AND LAMBDA - 10% SALARY INCREASE
raised_salaries = list(
    map(
        lambda emp: emp["salary"] * 1.10,
        employees
    )
)

print("Salaries after 10% raise:", raised_salaries)


# 8. FILTER - CHENNAI EMPLOYEES
chennai_employees = list(
    filter(
        lambda emp: emp["city"] == "Chennai",
        employees
    )
)

print(
    "Chennai:",
    [emp["name"] for emp in chennai_employees]
)


# 9. FOR LOOP WITH CONTINUE AND BREAK
print("\nLoop demonstration:")

for emp in employees:

    salary = emp["salary"]

    if salary == 0:
        continue

    if salary > 85000:
        break

    print(emp["name"], salary)


# 10. BONUS FUNCTION TESTING
print("\nBonus:", bonus(50000, 0.1, 1000, 2000))

print("Capped Bonus:", bonus(50000, 0.1, 1000, cap=4000))


# 11. EMPLOYEE OBJECT
print("\nEmployee Details:")

employee = Employee("Arun", 30000)

print(employee.get_details())

print("Annual Salary:", employee.annual_salary())


# 12. MANAGER OBJECT
print("\nManager Details:")

manager = Manager("Rahul", 80000, 5)

print(manager.get_details())


# 13. EXCEPTION HANDLING
print()

try:
    invalid_employee = Employee("Test", -500)

except InvalidSalaryError as e:
    print("Error:", e)

finally:
    print("Transaction finished")
