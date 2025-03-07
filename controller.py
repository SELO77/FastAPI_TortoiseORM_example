from fastapi import APIRouter, HTTPException
from typing import List

from models import User, Todo, TodoComment
from schemas import (
    UserCreate,
    UserResponse,
    TodoCreate,
    TodoUpdate,
    TodoResponse,
    HTTPNotFoundError,
    TodoCommentCreate,
    TodoCommentResponse,
    TodoCommentUpdate,
)

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "FastAPI with Tortoise ORM"}


# User endpoints
@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    user_obj = await User.create(username=user.username)
    return await UserResponse.from_tortoise_orm(user_obj)


@router.get("/users/", response_model=List[UserResponse])
async def get_users():
    return await UserResponse.from_queryset(User.all())


@router.get(
    "/users/{user_id}",
    response_model=UserResponse,
    responses={404: {"model": HTTPNotFoundError}},
)
async def get_user(user_id: int):
    return await UserResponse.from_queryset_single(User.get(id=user_id))


# Todo endpoints
@router.post("/todos/", response_model=TodoResponse)
async def create_todo(todo: TodoCreate):
    user = await User.get_or_none(id=todo.user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {todo.user_id} not found")

    todo_obj = await Todo.create(
        title=todo.title, description=todo.description, user_id=todo.user_id
    )
    return await TodoResponse.from_tortoise_orm(todo_obj)


@router.get("/todos/", response_model=List[TodoResponse])
async def get_todos():
    return await TodoResponse.from_queryset(Todo.all())


@router.get(
    "/todos/{todo_id}",
    response_model=TodoResponse,
    responses={404: {"model": HTTPNotFoundError}},
)
async def get_todo(todo_id: int):
    return await TodoResponse.from_queryset_single(Todo.get(id=todo_id))


@router.put(
    "/todos/{todo_id}",
    response_model=TodoResponse,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_todo(todo_id: int, todo: TodoUpdate):
    await Todo.filter(id=todo_id).update(**todo.model_dump(exclude_unset=True))
    return await TodoResponse.from_queryset_single(Todo.get(id=todo_id))


@router.delete("/todos/{todo_id}", responses={404: {"model": HTTPNotFoundError}})
async def delete_todo(todo_id: int):
    deleted_count = await Todo.filter(id=todo_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Todo {todo_id} not found")
    return {"message": f"Deleted todo {todo_id}"}


# TodoComment endpoints
@router.post("/todos/{todo_id}/comments/", response_model=TodoCommentResponse)
async def create_todo_comment(todo_id: int, comment: TodoCommentCreate):
    # Check if todo exists
    todo = await Todo.get_or_none(id=todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail=f"Todo {todo_id} not found")

    # Check if user exists
    user = await User.get_or_none(id=comment.user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {comment.user_id} not found")

    # Create comment
    comment_obj = await TodoComment.create(
        content=comment.content, todo_id=todo_id, user_id=comment.user_id
    )
    return await TodoCommentResponse.from_tortoise_orm(comment_obj)


@router.get("/todos/{todo_id}/comments/", response_model=List[TodoCommentResponse])
async def get_todo_comments(todo_id: int):
    # Check if todo exists
    todo = await Todo.get_or_none(id=todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail=f"Todo {todo_id} not found")

    return await TodoCommentResponse.from_queryset(TodoComment.filter(todo_id=todo_id))


@router.get(
    "/comments/{comment_id}",
    response_model=TodoCommentResponse,
    responses={404: {"model": HTTPNotFoundError}},
)
async def get_comment(comment_id: int):
    return await TodoCommentResponse.from_queryset_single(
        TodoComment.get(id=comment_id)
    )


@router.put(
    "/comments/{comment_id}",
    response_model=TodoCommentResponse,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_comment(comment_id: int, comment: TodoCommentUpdate):
    await TodoComment.filter(id=comment_id).update(
        **comment.model_dump(exclude_unset=True)
    )
    return await TodoCommentResponse.from_queryset_single(
        TodoComment.get(id=comment_id)
    )


@router.delete("/comments/{comment_id}", responses={404: {"model": HTTPNotFoundError}})
async def delete_comment(comment_id: int):
    deleted_count = await TodoComment.filter(id=comment_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Comment {comment_id} not found")
    return {"message": f"Deleted comment {comment_id}"}
