from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.courses.courses_schema import (
    GetCoursesQuerySchema,
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
    GetCoursesResponseSchema,
    GetCourseResponseSchema,
)


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Выполняет HTTP-запрос на получение списка курсов.

        Args:
            query: Схема параметров запроса на получение списка курсов.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.get(
            url="/api/v1/courses",
            params=query.model_dump(by_alias=True)
        )

    def get_course_api(self, course_id: str) -> Response:
        """
        Выполняет HTTP-запрос на получение курса.

        Args:
            course_id: Идентификатор курса.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.get(url=f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Выполняет HTTP-запрос на создание курса.

        Args:
            request: Схема запроса на создание курса.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.post(
            url="/api/v1/courses",
            json=request.model_dump(by_alias=True)
        )

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Выполняет HTTP-запрос на обновление курса.

        Args:
            course_id: Идентификатор курса.
            request: Схема запроса на обновление курса.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.patch(
            url=f"/api/v1/courses/{course_id}",
            json=request.model_dump(by_alias=True, exclude_none=True)
        )

    def delete_course_api(self, course_id: str) -> Response:
        """
        Выполняет HTTP-запрос на удаление курса.

        Args:
            course_id: Идентификатор курса.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.delete(url=f"/api/v1/courses/{course_id}")

    def get_courses(self, query: GetCoursesQuerySchema) -> GetCoursesResponseSchema:
        """
        Запрашивает список курсов и возвращает структурированный ответ.

        Args:
            query: Схема параметров запроса на получение списка курсов.

        Returns:
            Схема ответа на получение списка курсов.
        """
        response = self.get_courses_api(query)
        return GetCoursesResponseSchema.model_validate_json(response.text)


    def get_course(self, course_id: str) -> GetCourseResponseSchema:
        """
        Запрашивает курс и возвращает структурированный ответ.

        Args:
            course_id: Идентификатор курса.

        Returns:
            Схема ответа на получение курса.
        """
        response = self.get_course_api(course_id)
        return GetCourseResponseSchema.model_validate_json(response.text)

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Создает курс и возвращает структурированный ответ.

        Args:
            request: Схема запроса на создание курса.

        Returns:
            Схема ответа на создание курса.
        """
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

    def update_course(self, course_id: str, request: UpdateCourseRequestSchema) -> UpdateCourseResponseSchema:
        """
        Обновляет курс и возвращает структурированный ответ.

        Args:
            course_id: Идентификатор курса.
            request: Схема запроса на обновление курса.

        Returns:
            Схема ответа на обновление курса.
        """
        response = self.update_course_api(course_id, request)
        return UpdateCourseResponseSchema.model_validate_json(response.text)

    def delete_course(self, course_id: str) -> None:
        """
        Удаляет курс и возвращает ответ.

        Args:
            course_id: Идентификатор курса.
        """
        response = self.delete_course_api(course_id)
        return response.json()

def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    Returns:
        Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))