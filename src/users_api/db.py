from motor.motor_asyncio import AsyncIOMotorClient

from src.test_stage1.settings import (
    DATABASE_NAME,
    MONGODB_URL,
    USER_COLLECTION_NAME,
)


async def get_user_collection():
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client[DATABASE_NAME]
    collection = db[USER_COLLECTION_NAME]
    return collection
