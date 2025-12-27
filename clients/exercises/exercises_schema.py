from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class ExerciseSchema(BaseModel):
    """Схема данных задания."""
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore", default=100)
    min_score: int = Field(alias="minScore", default=10)
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesQuerySchema(BaseModel):
    """Схема параметров запроса на получение списка заданий для курса."""
    course_id: str = Field(alias="courseId")


class GetExercisesResponseSchema(BaseModel):
    """Схема ответа на получение списка заданий для курса."""
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """Схема ответа на получение задания."""
    exercise: ExerciseSchema

class CreateExerciseRequestSchema(BaseModel):
    """Схема запроса на создание задания."""
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class CreateExerciseResponseSchema(BaseModel):
    """Схема ответа на создание задания."""
    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    """Схема запроса на обновление задания."""
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateExerciseResponseSchema(BaseModel):
    """Схема ответа на обновление задания."""
    exercise: ExerciseSchema