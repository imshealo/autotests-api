import allure
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    GetExercisesResponseSchema,
    GetExerciseResponseSchema,
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)


class ExercisesClient(APIClient):
    """
    Клиент для работы c /api/v1/exercises
    """

    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Выполняет HTTP-запрос на получение списка заданий для курса.

        Args:
            query: Схема параметров запроса на получение списка заданий для курса.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.get(
            url="/api/v1/exercises",
            params=query.model_dump(by_alias=True)
        )

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Выполняет HTTP-запрос на создание задания.

        Args:
            request: Схема запроса на создание задания.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.post(
            url="/api/v1/exercises",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет HTTP-запрос на получение задания.

        Args:
            exercise_id: Идентификатор задания.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Выполняет HTTP-запрос на обновление задания.

        Args:
            exercise_id: Идентификатор задания.
            request: Схема запроса на обновление задания.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.patch(
            url=f"/api/v1/exercises/{exercise_id}",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет HTTP-запрос на удаление задания.

        Args:
            exercise_id: Идентификатор задания.

        Returns:
            HTTP-ответ от сервера.
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Запрашивает задание и возвращает структурированный ответ.

        Args:
            exercise_id: Идентификатор задания.

        Returns:
            Схема ответа на получение задания.
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Запрашивает список заданий и возвращает структурированный ответ.

        Args:
            query: Схема параметров запроса на получение списка заданий для курса.

        Returns:
            Схема ответа на получение списка заданий для курса.
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Создает курс и возвращает структурированный ответ.

        Args:
            request: Схема запроса на создание задания.

        Returns:
            Схема ответа на создание задания.
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Обновляет задание и возвращает структурированный ответ.

        Args:
            exercise_id: Идентификатор задания.
            request: Схема запроса на обновление задания.

        Returns:
            Схема ответа на обновление задания.
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

    def delete_exercise(self, exercise_id: str) -> None:
        """
        Удаляет задание и возвращает ответ.

        Args:
            exercise_id: Идентификатор задания.
        """
        response = self.delete_exercise_api(exercise_id)
        return response.json()

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    Returns:
        Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
