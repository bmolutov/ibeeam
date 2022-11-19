from bson.json_util import ObjectId

from schemas import ListUserProfilesSchema
from database import user_profiles_collection


async def get_user_profile(user_id: str):
    query = {"_id": ObjectId(user_id)}
    user_profile = await user_profiles_collection.find_one(query)
    return user_profile


async def list_user_profiles():
    user_profiles = []
    cursor = user_profiles_collection.find({})
    async for document in cursor:
        user_profiles.append(ListUserProfilesSchema(**document))
    return user_profiles
