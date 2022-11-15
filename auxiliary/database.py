import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
db = client.ibeeam
user_profiles_collection = db.user_profiles
