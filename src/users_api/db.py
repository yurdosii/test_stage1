from motor.motor_asyncio import AsyncIOMotorClient

from src.test_stage1.settings import (
    MONGODB_DATABASE_NAME,
    MONGODB_URL,
    MONGODB_USER_COLLECTION_NAME,
)


async def get_user_collection():
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client[MONGODB_DATABASE_NAME]
    collection = db[MONGODB_USER_COLLECTION_NAME]
    return collection
