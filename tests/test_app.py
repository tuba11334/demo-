import pytest
from httpx import AsyncClient
from app import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "Welcome to the Full Stack FastAPI App" in response.text

@pytest.mark.asyncio
async def test_get_data():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/data")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from the FastAPI API!"}
