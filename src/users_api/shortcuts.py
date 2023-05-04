from .enums import UserRoleEnum
from .models import User


def is_admin(user: User) -> bool:
    return user.role == UserRoleEnum.admin
