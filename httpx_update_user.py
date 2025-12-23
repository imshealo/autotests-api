import time

import httpx
from utils.fakers import get_random_email

# -------Create user---------
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
assert create_user_response.status_code == 200
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# -------Login---------
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
assert login_response.status_code == 200
login_response_data = login_response.json()
print('Login data:', login_response_data)

get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

# -------Patch user---------
patch_user_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

patch_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=get_user_headers,
    json=patch_user_payload
)
assert patch_user_response.status_code == 200
patch_user_response_data = patch_user_response.json()
print('Patch user data:', patch_user_response_data)
