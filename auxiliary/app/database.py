import motor.motor_asyncio

from settings import settings


client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)

db = client[settings.MONGO_INITDB_DATABASE]

user_profiles_collection = db.user_profiles
