from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с приватными методами /api/v1/users (требуется авторизация).
    """

    def _get_user_me_api(self) -> Response:
        """
        Выполняет HTTP-запрос на получение текущего пользователя.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.get(url="/api/v1/users/me")

    def _get_user_api(self, user_id: str) -> Response:
        """
        Выполняет HTTP-запрос на получение пользователя по идентификатору.

        Args:
            user_id: Идентификатор пользователя.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.get(url=f"/api/v1/users/{user_id}")

    def _update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Выполняет HTTP-запрос на обновление пользователя по идентификатору.

        Args:
            user_id: Идентификатор пользователя.
            request: Схема запроса на обновление пользователя.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.patch(
            url=f"/api/v1/users/{user_id}",
            json=request.model_dump(by_alias=True)
        )

    def _delete_user_api(self, user_id: str) -> Response:
        """
        Выполняет HTTP-запрос на удаление пользователя по идентификатору.

        Args:
            user_id: Идентификатор пользователя.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.delete(url=f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Запрашивает пользователя и возвращает структурированный ответ.

        Args:
            user_id: Идентификатор пользователя.

        Returns:
            Схема ответа на получение данных пользователя.
        """
        response = self._get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    Returns:
        Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))
