
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# Function to explain status codes
def explain_status(code):
    messages = {
        200: "OK - Request successful",
        201: "Created - Resource created successfully",
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error"
    }

    return messages.get(code, "Unknown status code")


# 1. GET request - First 5 users
response = requests.get(f"{BASE_URL}/users")

print("FIRST 5 USERS:")

if response.status_code == 200:
    users = response.json()

    for user in users[:5]:
        print(f'{user["id"]} - {user["name"]} - {user["email"]}')


# 2. POST request - Create a post
post_data = {
    "title": "My First Post",
    "body": "This is my first REST API request.",
    "userId": 1
}

response = requests.post(
    f"{BASE_URL}/posts",
    json=post_data
)

post_result = response.json()

print("\nPOST:", response.status_code, "id:", post_result["id"])


# 3. PUT request - Update complete post
put_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated post content",
    "userId": 1
}

put_response = requests.put(
    f"{BASE_URL}/posts/1",
    json=put_data
)


# 4. PATCH request - Update partial post
patch_data = {
    "title": "Partially Updated Title"
}

patch_response = requests.patch(
    f"{BASE_URL}/posts/1",
    json=patch_data
)


# 5. DELETE request
delete_response = requests.delete(
    f"{BASE_URL}/posts/1"
)

print(
    "PUT:", put_response.status_code,
    "| PATCH:", patch_response.status_code,
    "| DELETE:", delete_response.status_code
)


# 6. GET request - Check missing post
response = requests.get(f"{BASE_URL}/posts/9999")

if response.status_code == 404:
    print(f"GET /posts/9999 -> {response.status_code} Not found")


# 7. Explain different status codes
print("\nSTATUS CODE EXPLANATIONS:")

for code in [200, 201, 400, 401, 404, 500]:
    print(code, "-", explain_status(code))
