from bson.json_util import ObjectId

from database import user_profiles_collection


async def create_user_profile(user_profile):
    user_profile = await user_profiles_collection.insert_one(user_profile)
    return user_profile


async def update_user_profile(user_id, user_profile):
    await user_profiles_collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_profile})
    f = {"_id": 0}
    # TODO: resolve an issue
    updated_user_profile = await user_profiles_collection.find_one({"_id": ObjectId(user_id)}, f)
    return updated_user_profile


async def delete_user_profile(user_id):
    # TODO: finish implementing
    await user_profiles_collection.delete_one({"_id": ObjectId(user_id)})
    return True
