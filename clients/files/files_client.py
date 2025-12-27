from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    def _get_file_api(self, file_id: str) -> Response:
        """
        Выполняет HTTP-запрос на получение файла.

        Args:
            file_id: Идентификатор файла.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.get(url=f"/api/v1/files/{file_id}")

    def _create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Выполняет HTTP-запрос на создание файла.

        Args:
            request: Схема запроса на создание файла.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.post(
            url="/api/v1/files",
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={"upload_file": open(request.upload_file, 'rb')}
        )

    def _delete_file_api(self, file_id: str) -> Response:
        """
        Выполняет HTTP-запрос на удаление файла.

        Args:
            file_id: Идентификатор файла.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.delete(url=f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Создает файл и возвращает структурированный ответ.

        Args:
            request: Схема запроса на создание файла.

        Returns:
            Схема ответа на создание файла.
        """
        response = self._create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)


def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    Returns:
        Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))