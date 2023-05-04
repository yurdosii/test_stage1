from enum import Enum


class UserRoleEnum(str, Enum):
    admin = "admin"
    dev = "dev"
    mortal = "mortal"
