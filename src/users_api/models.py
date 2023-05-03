import datetime

from bson import ObjectId
from pydantic import BaseModel, Field, validator

from .enums import UserRole


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        # to fix 'ValueError: Value not declarable with JSON Schema'
        field_schema.update(type="string")


class UserBase(BaseModel):
    first_name: str
    last_name: str
    role: UserRole
    is_active: bool = True

    @validator("first_name")
    def name_must_not_contain_space(cls, value):
        if " " in value:
            raise ValueError("must not contain a space")
        return value


class UserCreate(UserBase):
    hashed_pass: str


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime.datetime
    last_login: datetime.datetime | None
    hashed_pass: str

    def dict(self, **kwargs):
        user_dict = super().dict(**kwargs)
        user_dict["id"] = user_dict.pop("_id")
        return user_dict

    class Config:
        json_encoders = {ObjectId: str}
