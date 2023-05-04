from unittest.mock import AsyncMock

import pytest
from httpx import AsyncClient

from src.main import app
from src.middlewares import verify_token


@pytest.mark.asyncio
async def test_db(async_mongodb):
    collection_names = await async_mongodb.list_collection_names()
    assert collection_names == ["users"]

    users = await async_mongodb.users.find().to_list(5)
    assert len(users) == 2


@pytest.mark.asyncio
async def test_get_users(mocker, async_mongodb):
    # mock
    collection_mock = AsyncMock(return_value=async_mongodb.users)
    mocker.patch(
        "src.users_api.crud.get_user_collection", side_effect=collection_mock
    )
    app.dependency_overrides[verify_token] = lambda: True

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(
            "/users/", headers={"Authorization": "Bearer token"}
        )

    assert response.status_code == 200

    users_data = response.json()
    assert len(users_data) == 2

    first_names = {user_data["first_name"] for user_data in users_data}
    assert "admin_name" in first_names
    assert "dev_name" in first_names
