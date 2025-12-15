import requests
import sys
import json
import time
import random

base_url = "http://localhost:8000/api"
random_id = int(time.time())
email = f"test_user_{random_id}@example.com"
password = "password123"
name = f"Test User {random_id}"

print(f"Attempting to register user: {email}")

try:
    resp = requests.post(f"{base_url}/auth/register", json={
        "email": email,
        "password": password,
        "name": name
    })
    
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.text}")
    
    if resp.status_code == 200:
        print("\n✅ Registration successful!")
        print(json.dumps(resp.json(), indent=2))
    else:
        print("\n❌ Registration failed")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
