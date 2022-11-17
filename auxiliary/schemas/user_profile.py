from typing import Optional, List
from datetime import date

from bson import ObjectId
from pydantic import BaseModel, HttpUrl, Field
from .base import PyObjectId, GenderEnum


class UserProfileBaseSchema(BaseModel):
    username: str
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    avatar: Optional[HttpUrl]
    gender: Optional[GenderEnum]
    bio: Optional[str]
    date_of_birth: Optional[date]
    # special fields:
    followers_ids: List[str] = []
    following_ids: List[str] = []
    blockers_ids: List[str] = []
    blocking_ids: List[str] = []
    favorite_posts_ids: List[int] = []


class ListUserProfilesSchema(BaseModel):
    username: str
    avatar: Optional[HttpUrl]

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class GetUserProfileSchema(UserProfileBaseSchema):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class CreateUserProfileRequestSchema(UserProfileBaseSchema):
    password: str


class CreateUserProfileResponseSchema(UserProfileBaseSchema):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class UpdateUserProfileRequestSchema(UserProfileBaseSchema):
    password: str


class UpdateUserProfileResponseSchema(UserProfileBaseSchema):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
