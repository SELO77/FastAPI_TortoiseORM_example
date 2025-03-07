from fastapi import FastAPI, HTTPException, Depends
from tortoise.contrib.fastapi import register_tortoise
from typing import List

from models import User, Todo
from schemas import (
    UserCreate,
    UserResponse,
    TodoCreate,
    TodoUpdate,
    TodoResponse,
    HTTPNotFoundError,
)
from database import TORTOISE_ORM

app = FastAPI(title="FastAPI Tortoise ORM Example")


@app.get("/")
async def root():
    return {"message": "FastAPI with Tortoise ORM"}


# User endpoints
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    user_obj = await User.create(username=user.username)
    return await UserResponse.from_tortoise_orm(user_obj)


@app.get("/users/", response_model=List[UserResponse])
async def get_users():
    return await UserResponse.from_queryset(User.all())


@app.get(
    "/users/{user_id}",
    response_model=UserResponse,
    responses={404: {"model": HTTPNotFoundError}},
)
async def get_user(user_id: int):
    return await UserResponse.from_queryset_single(User.get(id=user_id))


# Todo endpoints
@app.post("/todos/", response_model=TodoResponse)
async def create_todo(todo: TodoCreate):
    user = await User.get_or_none(id=todo.user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {todo.user_id} not found")

    todo_obj = await Todo.create(
        title=todo.title, description=todo.description, user_id=todo.user_id
    )
    return await TodoResponse.from_tortoise_orm(todo_obj)


@app.get("/todos/", response_model=List[TodoResponse])
async def get_todos():
    return await TodoResponse.from_queryset(Todo.all())


@app.get(
    "/todos/{todo_id}",
    response_model=TodoResponse,
    responses={404: {"model": HTTPNotFoundError}},
)
async def get_todo(todo_id: int):
    return await TodoResponse.from_queryset_single(Todo.get(id=todo_id))


@app.put(
    "/todos/{todo_id}",
    response_model=TodoResponse,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_todo(todo_id: int, todo: TodoUpdate):
    await Todo.filter(id=todo_id).update(**todo.model_dump(exclude_unset=True))
    return await TodoResponse.from_queryset_single(Todo.get(id=todo_id))


@app.delete("/todos/{todo_id}", responses={404: {"model": HTTPNotFoundError}})
async def delete_todo(todo_id: int):
    deleted_count = await Todo.filter(id=todo_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Todo {todo_id} not found")
    return {"message": f"Deleted todo {todo_id}"}


# Register Tortoise ORM
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
