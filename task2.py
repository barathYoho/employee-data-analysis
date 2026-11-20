
import csv
import json
import os
import requests

from dotenv import load_dotenv


# ==========================================
# TASK 2: FILES, APIs AND ENVIRONMENT
# ==========================================


# 1. LOAD ENVIRONMENT VARIABLES

load_dotenv()

API_KEY = os.getenv("API_KEY")

if API_KEY:
    print("API_KEY loaded successfully.")
else:
    print("Warning: API_KEY not found in .env file.")


# 2. READ EMPLOYEES.CSV USING csv.DictReader

with open("employees.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

# Convert salary into integer
for emp in employees:
    emp["salary"] = int(emp["salary"])


# 3. WRITE EMPLOYEES.JSON

with open("employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

print("Employee data saved to employees.json")


# 4. CREATE HIGH_EARNERS.CSV
# Employees with salary above 50000

high_earners = [
    emp for emp in employees
    if emp["salary"] > 50000
]

with open("high_earners.csv", "w", newline="", encoding="utf-8") as file:

    fieldnames = ["id", "name", "department", "salary", "city"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(high_earners)

print(
    f"Rows read: {len(employees)} | "
    f"High earners: {len(high_earners)}"
)


# 5. GET API DATA USING REQUESTS

api_url = "https://jsonplaceholder.typicode.com/users"

try:

    response = requests.get(api_url, timeout=5)

    response.raise_for_status()

    users = response.json()

    print("\nFirst 3 API Users:")

    for user in users[:3]:
        print(
            f'{user.get("id")} - '
            f'{user.get("name")} - '
            f'{user.get("email")}'
        )


    # 6. PARSE NESTED JSON USING .get()

    user_details = []

    for user in users:

        address = user.get("address", {})
        geo = address.get("geo", {})

        user_details.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": address.get("city"),
            "latitude": geo.get("lat"),
            "longitude": geo.get("lng")
        })


    # 7. SAVE NESTED JSON DATA TO users.json

    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(user_details, file, indent=4)

    print("\nAPI data saved to users.json")


except requests.exceptions.Timeout:
    print("Error: API request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the API.")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except requests.exceptions.RequestException as error:
    print("API Error:", error)


# 8. TEST HTTP 404 ERROR

try:

    error_url = "https://jsonplaceholder.typicode.com/users/9999"

    error_response = requests.get(error_url, timeout=5)

    if error_response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        error_response.raise_for_status()
        print("/users/9999 ->", error_response.status_code)

except requests.exceptions.Timeout:
    print("Error: 404 test request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect during 404 test.")

except requests.exceptions.RequestException as error:
    print("Request Error:", error)
