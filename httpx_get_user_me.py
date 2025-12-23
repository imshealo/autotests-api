import httpx
from pprint import pprint

def auth():
    payload = {
        "email": "zyablik@example.com",
        "password": "bimbimbambam"
    }

    try:
        response = httpx.post(
            url="http://localhost:8000/api/v1/authentication/login",
            json=payload)
        response.raise_for_status()

        pprint({
            "status_code": response.status_code,
            "body": response.json()
        })

        return response.json()["token"]["accessToken"]

    except httpx.HTTPStatusError as e:
        pprint(f"HTTPStatusError: {e}")


def get_me(auth_token: str):

    try:
        response = httpx.get(
            url="http://localhost:8000/api/v1/users/me",
            headers={"Authorization": f"Bearer {auth_token}"}
        )
        response.raise_for_status()

        pprint({
            "status_code": response.status_code,
            "body": response.json()
        })

    except httpx.HTTPStatusError as e:
        pprint(f"HTTPStatusError: {e}")


if __name__ == "__main__":
    token = auth()
    get_me(token)