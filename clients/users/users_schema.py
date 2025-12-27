from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserSchema(BaseModel):
    """Схема данных пользователя."""
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """Схема запроса на создание пользователя."""
    # model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str = Field(min_length=8, max_length=16)
    last_name: str = Field(alias="lastName", default="string")
    first_name: str = Field(alias="firstName", default="string")
    middle_name: str = Field(alias="middleName", default="string")


class CreateUserResponseSchema(BaseModel):
    """Схема ответа на создание пользователя."""
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """Схема запроса на обновление пользователя."""
    email: EmailStr | None
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")


class UpdateUserResponseSchema(BaseModel):
    """Схема ответа на обновление пользователя."""
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """Схема ответа на получение данных пользователя."""
    user: UserSchema
