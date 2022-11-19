from bson import ObjectId
from pydantic import BaseModel, HttpUrl, Field
from .base import PyObjectId, GenderEnum


class LoginSchema(BaseModel):
    user_id: str
    password: str


class GetUserCredSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    password: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
