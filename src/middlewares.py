from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError

from src.test_stage1.settings import ALGORITHM, SECRET_KEY
from src.users_api.crud import get_user_by_id
from src.users_api.models import User
from src.users_api.shortcuts import is_admin

from .models import PyObjectId

security = HTTPBearer()


async def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> User:
    token = credentials.credentials
    token_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: PyObjectId = PyObjectId.validate(payload.get("sub"))
    except (JWTError, ValueError):
        raise token_exception

    user = await get_user_by_id(id=user_id)
    if user is None:
        raise token_exception

    return user


async def verify_admin(
    user: User = Depends(verify_token),
) -> User:
    if not is_admin(user):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return user
