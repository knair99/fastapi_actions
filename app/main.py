from fastapi import FastAPI, HTTPException
from typing import List
from .models import Task
from typing import Dict

app = FastAPI()

# In-memory list to hold the tasks
tasks = []

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    # Return all tasks
    return tasks

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task.id == task_id:
            task.title = updated_task.title
            task.completed = updated_task.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")
