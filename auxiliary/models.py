import enum
from typing import Optional
from datetime import date

from bson import ObjectId
from pydantic import BaseModel, HttpUrl, Field


class GenderEnum(str, enum.Enum):
    """
    Type of gender
    """
    male = 'Male'
    female = 'Female'
    another = 'Another'
    
    
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
        field_schema.update(type="string")


class CreateGetUpdateUserProfile(BaseModel):
    email: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    avatar: Optional[HttpUrl]
    gender: Optional[GenderEnum]
    bio: Optional[str]
    date_of_birth: Optional[date]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class ListUserProfile(CreateGetUpdateUserProfile):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
