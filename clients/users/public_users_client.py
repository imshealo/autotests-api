from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient


class CreateUserRequest(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными методами API /users
    """

    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Метод создает нового пользователя.

        :param request: Словарь CreateUserRequest
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url="http://localhost:8000/api/v1/users",
            json=request
        )
