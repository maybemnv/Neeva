import requests
import time

url = "http://localhost:8000/auth/register"
data = {
    "email": f"test_error_{int(time.time())}@example.com",
    "password": "Password123",
    "name": "Test Error Trigger"
}

try:
    print(f"Sending POST request to {url} with data: {data}")
    response = requests.post(url, json=data)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
except Exception as e:
    print(f"Request failed: {e}")
