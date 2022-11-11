import motor.motor_asyncio

from models import ListUpdateUserProfile


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
db = client.ibeeam
users_collection = db.users


async def get_user_profile(user_id: str):
    user = await users_collection.find_one({"_id": user_id})
    return user


async def list_user_profiles():
    users = []
    cursor = users_collection.find({})
    async for document in cursor:
        users.append(ListUpdateUserProfile(**document))
    return users


async def create_user_profile(user):
    document = user
    result = await users_collection.insert_one(document)
    return result


async def update_user_profile(user_id, user_profile):
    await users_collection.update_one({"_id": user_id}, {"$set": user_profile})
    print(user_id, user_profile)
    updated_user_profile = await users_collection.find_one({"_id": user_id})
    return updated_user_profile


async def delete_user_profile(user_id):
    await users_collection.delete_one({"_id": user_id})
    return True
