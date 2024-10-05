import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_and_update_task():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create a new task
        response = await ac.post("/tasks", json={"id": 1, "title": "New Task", "completed": False})
        assert response.status_code == 200
        task = response.json()
        assert task["title"] == "New Task"
        assert task["completed"] is False

        # Update the task
        response = await ac.put("/tasks/1", json={"id": 1, "title": "Updated Task", "completed": True})
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["title"] == "Updated Task"
        assert updated_task["completed"] is True
