from httpx import Client
from pydantic import BaseModel
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema


class AuthenticationUserSchema(BaseModel):
    """Схема учетных данных пользователя для аутентификации."""
    email: str
    password: str


# Создаем private builder
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Создаёт HTTP-клиент с аутентификацией пользователя.

    Args:
        user: Схема учетных данных пользователя для аутентификации.

    Returns:
        Готовый к использованию HTTP-клиент с аутентификацией.
    """
    authentication_client = get_authentication_client()
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=1,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )
