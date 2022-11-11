import enum
from typing import Optional
from datetime import date

from pydantic import BaseModel, HttpUrl


class GenderEnum(str, enum.Enum):
    """
    Type of gender
    """
    male = 'Male'
    female = 'Female'
    another = 'Another'


class UserProfile(BaseModel):
    id: int
    email: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    avatar: Optional[HttpUrl]
    gender: Optional[GenderEnum]
    bio: Optional[str]
    date_of_birth: Optional[date]
