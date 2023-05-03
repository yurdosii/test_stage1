import datetime

from fastapi import APIRouter, HTTPException, status

from src.test_stage1.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from src.users_api.crud import get_user_by_first_name, update_user_by_id

from .models import Token, UserAuth
from .shortcuts import create_access_token, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])


async def authenticate_user(first_name: str, password: str):
    user = await get_user_by_first_name(first_name)
    if not user:
        return False
    if not verify_password(password, user.hashed_pass):
        return False
    return user


@router.post("/access_token", response_model=Token)
async def get_access_token(auth_data: UserAuth):
    user = await authenticate_user(auth_data.first_name, auth_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # update last_login datetime
    user.last_login = datetime.datetime.now()
    await update_user_by_id(user.id, user)

    access_token_expires = datetime.timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
