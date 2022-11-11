import motor.motor_asyncio

from models import UserProfile


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.ibeeam
collection = database.users


async def get_user_profile(user_id: int):
    user = await collection.find_one({"id": user_id})
    return user


async def list_user_profiles():
    users = []
    cursor = collection.find({})
    async for document in cursor:
        users.append(UserProfile(**document))
    return users


async def create_user_profile(user):
    document = user
    result = await collection.insert_one(document)
    return document


async def update_user_profile(updated_user):
    await collection.update_one(updated_user)
    document = await collection.find_one({"id": updated_user["id"]})
    return document


async def delete_user_profile(user_id):
    await collection.delete_one({"id": user_id})
    return True
