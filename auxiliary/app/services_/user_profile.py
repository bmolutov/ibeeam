from bson.json_util import ObjectId

from database import user_profiles_collection


async def create_user_profile(user_profile):
    user_profile = await user_profiles_collection.insert_one(user_profile)
    return user_profile


async def update_user_profile(username, user_profile):
    await user_profiles_collection.update_one({"username": username}, {"$set": user_profile})
    # TODO: resolve an issue
    updated_user_profile = await user_profiles_collection.find_one({"username": username})
    return updated_user_profile


async def delete_user_profile(username):
    # TODO: finish implementing
    await user_profiles_collection.delete_one({"username": username})
    return True
