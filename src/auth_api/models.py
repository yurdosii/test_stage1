from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserAuth(BaseModel):
    first_name: str  # first_name should be unique
    password: str
