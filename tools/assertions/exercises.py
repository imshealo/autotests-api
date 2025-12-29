from clients.exercises.exercises_schema import (
    ExerciseSchema,
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema,
)
from tools.assertions.base import assert_equal


def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: CreateExerciseResponseSchema):
    """
    Проверяет, что ответ на создание задания соответствует запросу.

    Args:
        request: Исходный запрос на создание задания.
        response: Ответ API с данными задания.

    Raises:
        AssertionError: Если хотя бы одно поле не совпадает.
    """

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные задания соответствуют ожидаемым.

    Args:
        actual: Фактические данные задания.
        expected: Ожидаемые данные задания.

    Raises:
        AssertionError: Если хотя бы одно поле не совпадает.
    """

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение задания соответствует ответу на создание задания.

    Args:
        get_exercise_response: Ответ API при запросе списка курсов.
        create_exercise_response: Список API ответов при создании курсов.

    Raises:
        AssertionError: Если данные курсов не совпадают.
    """

    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)
