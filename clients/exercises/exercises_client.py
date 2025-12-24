from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient


class GetExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий для определенного курса.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы c /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesRequestDict) -> Response:
        """
        Метод получения списка заданий для определенного курса.

        :param query: Словарь GetExercisesRequestDict
        :return: Объект httpx.Response
        """
        return self.get(
            url="/api/v1/exercises",
            params=query,
        )

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания информации о задании по exercise_id.

        :param request: Словарь CreateExerciseRequestDict
        :return: Объект httpx.Response
        """
        return self.post(
            url="/api/v1/exercise",
            json=request
        )

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании по exercise_id.

        :param exercise_id: Идентификатор задания
        :return: Объект httpx.Response
        """
        return self.get(
            url=f"/api/v1/exercise/{exercise_id}",
        )

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления данных задания.

        :param exercise_id: Идентификатор задания
        :param request: Словарь UpdateExerciseRequestDict
        :return: Объект httpx.Response
        """
        return self.patch(
            url=f"/api/v1/exercise/{exercise_id}",
            json=request
        )

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания
        :return: Объект httpx.Response
        """
        return self.delete(
            url=f"/api/v1/exercise/{exercise_id}",
        )
