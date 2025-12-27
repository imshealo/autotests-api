from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    """Схема аутентификационных токенов."""
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestSchema(BaseModel):
    """Схема запроса на аутентификацию."""
    email: str
    password: str


class LoginResponseSchema(BaseModel):
    """Схема ответа на аутентификацию."""
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """Схема запроса на обновление токена."""
    refresh_token: str = Field(alias="refreshToken")
