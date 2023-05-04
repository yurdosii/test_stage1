import datetime

from pymongo import ReturnDocument

from src.auth_api.shortcuts import get_password_hash

from .db import get_user_collection
from .models import PyObjectId, User, UserCreate, UserUpdate


async def create_user(user: UserCreate) -> User:
    now = datetime.datetime.now()

    user_data = dict(user)
    user_data["created_at"] = now
    user_data["last_login"] = now
    user_data["hashed_pass"] = get_password_hash(user.password)

    collection = await get_user_collection()
    result = await collection.insert_one(user_data)
    db_user = await collection.find_one({"_id": result.inserted_id})

    return db_user


async def update_user_by_id(id: PyObjectId, user: UserUpdate) -> User:
    collection = await get_user_collection()
    db_user = await collection.find_one_and_update(
        {"_id": id},
        {"$set": dict(user)},
        return_document=ReturnDocument.AFTER,
    )
    if db_user:
        db_user = User(**db_user)
    return db_user


async def delete_user(id: PyObjectId) -> bool:
    collection = await get_user_collection()
    delete_result = await collection.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return True
    return False


async def get_users(limit: int) -> list[User]:
    collection = await get_user_collection()
    db_users = await collection.find().to_list(limit)
    return db_users


async def get_user_by_id(id: PyObjectId) -> User | None:
    collection = await get_user_collection()
    db_user = await collection.find_one({"_id": id})
    if db_user:
        db_user = User(**db_user)
    return db_user


async def get_user_by_first_name(first_name: str) -> User | None:
    collection = await get_user_collection()
    db_user = await collection.find_one({"first_name": first_name})
    if db_user:
        db_user = User(**db_user)
    return db_user
