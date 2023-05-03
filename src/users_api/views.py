from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response

from src.middlewares import verify_admin, verify_token

from . import crud
from .models import PyObjectId, User, UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    return await crud.create_user(user)


@router.put("/{id}", response_model=User)
async def update_user_by_id(
    id: PyObjectId,
    user: UserUpdate,
    _: str = Depends(verify_admin),
):
    db_user = await crud.update_user_by_id(id, user)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return db_user


@router.delete("/{id}")
async def delete_user(
    id: PyObjectId,
    _: str = Depends(verify_token),
):
    result = await crud.delete_user(id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/", response_model=list[User])
async def get_users(
    limit: int = 100,
    _: str = Depends(verify_token),
):
    return await crud.get_users(limit)


@router.get("/{id}", response_model=User)
async def get_user_by_id(
    id: PyObjectId,
    _: str = Depends(verify_token),
):
    db_user = await crud.get_user_by_id(id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return db_user
