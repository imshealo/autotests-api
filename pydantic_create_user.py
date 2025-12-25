from pydantic import BaseModel, Field, EmailStr



class UserSchema(BaseModel):
    """
    Схема данных пользователя
    """
    id: int
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса на создание пользователя
    """
    email: EmailStr
    password: str = Field(min_length=8, max_length=16)
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа на создание пользователя
    """
    user: UserSchema