from pydantic import BaseModel, HttpUrl


class FileSchema(BaseModel):
    """Схема структуры файла."""
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """Схема запроса на создание файла."""
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """Схема ответа на создание файла."""
    file: FileSchema
