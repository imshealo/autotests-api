import allure
from httpx import Response
from clients.api_client import APIClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema, RefreshRequestSchema
from clients.public_http_builder import get_public_http_client



class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Выполняет HTTP-запрос аутентификации пользователя.

        Args:
            request: Схема запроса на аутентификацию.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.post(
            url="/api/v1/authentication/login",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Refresh authentication token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Выполняет HTTP-запрос обновления токена авторизации.

        Args:
            request: Схема запроса на обновление токена.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.post(
            url="/api/v1/authentication/refresh",
            json=request.model_dump(by_alias=True)
        )

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """
        Выполняет аутентификацию пользователя и возвращает структурированный ответ.

        Args:
            request: Схема запроса на аутентификацию.

        Returns:
            Схема ответа на аутентификацию.
        """
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    Returns:
        Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
