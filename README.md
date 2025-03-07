# FastAPI with Tortoise ORM Example

A simple RESTful API built with FastAPI and Tortoise ORM.

## Features

- User and Todo models with relationship
- CRUD operations for both models
- SQLite database
- Automatic schema generation
- Pydantic models for request/response validation

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the application with:

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Users
- `GET /users/` - List all users
- `POST /users/` - Create a new user
- `GET /users/{user_id}` - Get a specific user

### Todos
- `GET /todos/` - List all todos
- `POST /todos/` - Create a new todo
- `GET /todos/{todo_id}` - Get a specific todo
- `PUT /todos/{todo_id}` - Update a todo
- `DELETE /todos/{todo_id}` - Delete a todo 