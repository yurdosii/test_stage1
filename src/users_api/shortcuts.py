from .enums import UserRole
from .models import User


def is_admin(user: User) -> bool:
    return user.role == UserRole.admin
