import requests
import sys
import json

# Login to get token
base_url = "http://localhost:8000/api"
email = "test4@example.com"
password = "password123"

try:
    resp = requests.post(f"{base_url}/auth/login", data={"username": email, "password": password})
    if resp.status_code != 200:
        print(f"Login failed: {resp.text}")
        sys.exit(1)
    
    token = resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Send chat message
    chat_resp = requests.post(f"{base_url}/chat/", json={"message": "Hello"}, headers=headers)
    print(f"Status: {chat_resp.status_code}")
    print(f"Response: {chat_resp.text}")
    
    if chat_resp.status_code == 200:
        print("\n✅ Chat is working!")
        print(json.dumps(chat_resp.json(), indent=2))
    else:
        print("\n❌ Chat failed")
        try:
            error_detail = chat_resp.json()
            print(f"Error detail: {json.dumps(error_detail, indent=2)}")
        except:
            pass

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
