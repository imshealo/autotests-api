from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными методами /api/v1/users (без авторизации).
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Выполняет HTTP-запрос на создание пользователя.

        Args:
            request: Схема запроса на создание пользователя.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.post(
            url="/api/v1/users",
            json=request.model_dump(by_alias=True)
        )

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Создает пользователя и возвращает структурированный ответ.

        Args:
            request: Схема запроса на создание пользователя.

        Returns:
            Схема ответа на создание пользователя.
        """
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    Returns:
        Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())