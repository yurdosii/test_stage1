import datetime

from bson import ObjectId
from pydantic import BaseModel, Field, validator

from src.models import PyObjectId

from .enums import UserRole


class UserBase(BaseModel):
    first_name: str = Field(..., max_length=64)
    last_name: str = Field(..., max_length=64)
    role: UserRole
    is_active: bool = True

    @validator("first_name")
    def name_must_not_contain_space(cls, value):
        if " " in value:
            raise ValueError("must not contain a space")
        return value


class UserCreate(UserBase):
    password: str = Field(..., min_length=4)


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime.datetime
    last_login: datetime.datetime
    hashed_pass: str

    def dict(self, **kwargs):
        user_dict = super().dict(**kwargs)
        user_dict["id"] = user_dict.pop("_id")
        return user_dict

    class Config:
        json_encoders = {ObjectId: str}
