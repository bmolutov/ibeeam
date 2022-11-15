import enum

from bson import ObjectId


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
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
