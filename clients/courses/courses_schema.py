from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


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
    user_id: str = Field(alias="userId")


class GetCoursesResponseSchema(BaseModel):
    """Схема ответа на получение списка курсов."""
    courses: list[CourseSchema]

class CreateCourseRequestSchema(BaseModel):
    """Схема запроса на создание курса."""
    model_config = ConfigDict(populate_by_name=True)

    title: str = "Python"
    max_score: int = Field(alias="maxScore", default=300)
    min_score: int = Field(alias="minScore", default=90)
    description: str = "Python API course"
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class CreateCourseResponseSchema(BaseModel):
    """Схема ответа на создание курса."""
    course: CourseSchema


class GetCourseResponseSchema(BaseModel):
    """Схема ответа на получение курса."""
    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    """Схема запроса на обновление курса."""
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateCourseResponseSchema(BaseModel):
    """Схема ответа на обновление курса."""
    course: CourseSchema
