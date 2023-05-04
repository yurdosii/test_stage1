import datetime

import pytest

from src.users_api.models import User
from src.users_api.shortcuts import is_admin


@pytest.fixture(scope="function")
def admin_user():
    return User(
        first_name="yurii",
        last_name="last",
        role="admin",
        is_active=True,
        created_at=datetime.datetime.now(),
        last_login=datetime.datetime.now(),
        hashed_pass="hashed_passwords",
    )


@pytest.fixture(scope="function")
def dev_user():
    return User(
        first_name="yurko",
        last_name="first",
        role="dev",
        is_active=True,
        created_at=datetime.datetime.now(),
        last_login=datetime.datetime.now(),
        hashed_pass="hashed_passwords",
    )


@pytest.mark.parametrize(
    "user, expected", (("admin_user", True), ("dev_user", False))
)
def test_is_admin(request, user, expected):
    user = request.getfixturevalue(user)
    assert is_admin(user) == expected
