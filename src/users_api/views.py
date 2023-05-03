from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from . import crud
from .models import PyObjectId, User, UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    return await crud.create_user(user)


@router.put("/{id}", response_model=User)
async def update_user_by_id(id: PyObjectId, user: UserUpdate):
    db_user = await crud.update_user_by_id(id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/{id}")
async def delete_user(id: PyObjectId):
    result = await crud.delete_user(id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return Response(status_code=204)


@router.get("/", response_model=list[User])
async def get_users(limit: int = 100):
    return await crud.get_users(limit)


@router.get("/{id}", response_model=User)
async def get_user_by_id(id: PyObjectId):
    db_user = await crud.get_user_by_id(id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
