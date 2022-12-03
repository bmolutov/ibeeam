from bson import ObjectId
from pydantic import BaseModel, HttpUrl, Field
from .base import PyObjectId, GenderEnum


class LoginSchema(BaseModel):
    username: str
    password: str


class GetUserCredSchema(BaseModel):
    username: str
    password: str
