from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator
from models import User, Todo, TodoComment


# Pydantic models for request
class UserCreate(BaseModel):
    username: str


class TodoCreate(BaseModel):
    title: str
    description: str
    user_id: int


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class TodoCommentCreate(BaseModel):
    content: str
    todo_id: int
    user_id: int


class TodoCommentUpdate(BaseModel):
    content: str


# Error response model
class HTTPNotFoundError(BaseModel):
    detail: str


# Pydantic models generated from Tortoise models
UserResponse = pydantic_model_creator(User, name="UserResponse")
TodoResponse = pydantic_model_creator(Todo, name="TodoResponse")
TodoCommentResponse = pydantic_model_creator(TodoComment, name="TodoCommentResponse")
