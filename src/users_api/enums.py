from enum import Enum


class UserRole(str, Enum):
    admin = "admin"
    dev = "dev"
    mortal = "mortal"
