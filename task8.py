
import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API key
API_KEY = os.getenv("API_KEY")


# 1. GET request with API key
try:
    headers = {
        "X-API-Key": API_KEY
    }

    response = requests.get(
        "https://httpbin.org/headers",
        headers=headers,
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    received_key = data.get("headers", {}).get("X-Api-Key")

    print("Server received key:", received_key)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error occurred")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)


# 2. Test timeout with delay API
try:
    response = requests.get(
        "https://httpbin.org/delay/10",
        timeout=3
    )

    response.raise_for_status()

except requests.exceptions.Timeout:
    print("Timeout after 3 seconds: please try again")

except requests.exceptions.ConnectionError:
    print("Connection error occurred")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)


# 3. Handle HTTP 500 error
try:
    response = requests.get(
        "https://httpbin.org/status/500",
        timeout=5
    )

    response.raise_for_status()

except requests.exceptions.HTTPError:
    print("Server error 500 handled")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error occurred")


# 4. Parse nested JSON using get()
nested_data = {
    "user": {
        "id": 101,
        "name": "Arun",
        "address": {
            "city": "Chennai",
            "country": "India"
        }
    }
}

user = nested_data.get("user", {})
address = user.get("address", {})

result = {
    "id": user.get("id"),
    "name": user.get("name"),
    "city": address.get("city"),
    "country": address.get("country")
}


# 5. Save result to result.json
with open("result.json", "w") as file:
    json.dump(result, file, indent=2)

print("\nNested JSON saved to result.json")


# 6. Read result.json
with open("result.json", "r") as file:
    saved_data = json.load(file)

print("Saved JSON:", saved_data)
