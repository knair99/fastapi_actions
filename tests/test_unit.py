from app.main import tasks, create_task, update_task
from app.models import Task
import pytest


@pytest.fixture
def task_data():
    return Task(id=1, title="Test Task", completed=False)


@pytest.mark.asyncio
async def test_create_task(task_data):
    # Test creating a task
    tasks.clear()  # Clear the tasks before testing
    await create_task(task_data)
    assert len(tasks) == 1
    assert tasks[0].title == "Test Task"


@pytest.mark.asyncio
async def test_update_task(task_data):
    tasks.clear()
    await create_task(task_data)
    updated_task = Task(id=1, title="Updated Task", completed=True)
    await update_task(1, updated_task)

    assert tasks[0].title == "Updated Task"
    assert tasks[0].completed is True
