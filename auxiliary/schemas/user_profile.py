from typing import Optional
from datetime import date

from bson import ObjectId
from pydantic import BaseModel, HttpUrl, Field
from .base import PyObjectId, GenderEnum


class ListUserProfilesSchema(BaseModel):
    email: str
    avatar: Optional[HttpUrl]

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class GetUserProfileSchema(BaseModel):
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    avatar: Optional[HttpUrl]
    gender: Optional[GenderEnum]
    bio: Optional[str]
    date_of_birth: Optional[date]

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class CreateUserProfileRequestSchema(BaseModel):
    email: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    avatar: Optional[HttpUrl]
    gender: Optional[GenderEnum]
    bio: Optional[str]
    date_of_birth: Optional[date]


class CreateUserProfileResponseSchema(BaseModel):
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    avatar: Optional[HttpUrl]
    gender: Optional[GenderEnum]
    bio: Optional[str]
    date_of_birth: Optional[date]

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class UpdateUserProfileRequestSchema(BaseModel):
    email: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    avatar: Optional[HttpUrl]
    gender: Optional[GenderEnum]
    bio: Optional[str]
    date_of_birth: Optional[date]


class UpdateUserProfileResponseSchema(BaseModel):
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    avatar: Optional[HttpUrl]
    gender: Optional[GenderEnum]
    bio: Optional[str]
    date_of_birth: Optional[date]

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
