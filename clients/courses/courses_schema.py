from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class CourseSchema(BaseModel):
    """Схема данных курса."""
    id: str
    title: str
    max_score: int = Field(alias="maxScore", default=100)
    min_score: int = Field(alias="minScore", default=10)
    description: str = "Playwright course"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCoursesQuerySchema(BaseModel):
    """Схема параметров запроса на получение списка курсов."""
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class GetCoursesResponseSchema(BaseModel):
    """Схема ответа на получение списка курсов."""
    courses: list[CourseSchema]

class CreateCourseRequestSchema(BaseModel):
    """Схема запроса на создание курса."""
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)


class CreateCourseResponseSchema(BaseModel):
    """Схема ответа на создание курса."""
    course: CourseSchema


class GetCourseResponseSchema(BaseModel):
    """Схема ответа на получение курса."""
    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    """Схема запроса на обновление курса."""
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateCourseResponseSchema(BaseModel):
    """Схема ответа на обновление курса."""
    course: CourseSchema
