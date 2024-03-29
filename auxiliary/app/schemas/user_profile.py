from typing import Optional, List
from datetime import date

from pydantic import BaseModel, HttpUrl
from .base import GenderEnum


class UserProfileBaseSchema(BaseModel):
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    avatar: Optional[HttpUrl]
    gender: Optional[GenderEnum]
    bio: Optional[str]
    date_of_birth: Optional[date]
    # special fields:
    followers: List[str] = []
    following: List[str] = []
    blockers: List[str] = []
    blocking: List[str] = []
    favorite_posts_ids: List[int] = []


class ListUserProfilesSchema(BaseModel):
    username: str
    email: str
    avatar: Optional[HttpUrl]
    first_name: Optional[str]
    last_name: Optional[str]
    password: str


class GetUserProfileSchema(UserProfileBaseSchema):
    username: str


class CreateUserProfileRequestSchema(UserProfileBaseSchema):
    username: str
    password: str


class CreateUserProfileResponseSchema(UserProfileBaseSchema):
    username: str


class UpdateUserProfileRequestSchema(UserProfileBaseSchema):
    password: str


class UpdateUserProfileResponseSchema(UserProfileBaseSchema):
    username: str
