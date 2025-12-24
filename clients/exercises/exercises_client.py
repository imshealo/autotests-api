from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesRequestQuery(TypedDict):
    """
    Описание структуры запроса на получение списка заданий для определенного курса.
    """
    courseId: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение списка заданий для определенного курса.
    """
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение задания.
    """
    exercise: Exercise

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


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на создание задания.
    """
    exercise: Exercise

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


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на обновление задания.
    """
    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы c /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesRequestQuery) -> Response:
        """
        Метод получения списка заданий для определенного курса.

        :param query: Словарь GetExercisesRequestQuery
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
            url="/api/v1/exercises",
            json=request
        )

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании по exercise_id.

        :param exercise_id: Идентификатор задания
        :return: Объект httpx.Response
        """
        return self.get(url=f"/api/v1/exercise/{exercise_id}")

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
        return self.delete(url=f"/api/v1/exercise/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод обертка над get_exercise_api для возврата структурированных данных.

        :param exercise_id: Идентификатор задания
        :return: Словарь GetExerciseResponseDict
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesRequestQuery) -> GetExercisesResponseDict:
        """
        Метод обертка над get_exercises_api для возврата структурированных данных.

        :param query: Словарь GetExercisesRequestQuery
        :return: Словарь GetExercisesResponseDict
        """
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод обертка над create_exercise_api для возврата структурированных данных.

        :param request: Словарь CreateExerciseRequestDict
        :return: Словарь CreateExerciseResponseDict
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод обертка над update_exercise_api для возврата структурированных данных.

        :param exercise_id: Идентификатор задания
        :param request: Словарь UpdateExerciseRequestDict
        :return: Словарь UpdateExerciseResponseDict
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
