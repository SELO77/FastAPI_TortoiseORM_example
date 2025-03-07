# FastAPI with TortoiseORM Example

This is a simple example of a FastAPI application using TortoiseORM for database operations and Aerich for migrations.

## Features

- FastAPI for the web framework
- TortoiseORM for the ORM
- SQLite for the database
- Aerich for database migrations
- Pydantic for data validation

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/fastapi-tortoise-example.git
cd fastapi-tortoise-example

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Database Migrations

This project uses Aerich for database migrations. See [AERICH_README.md](AERICH_README.md) for detailed instructions.

Quick commands:

```bash
# Initialize Aerich (already done)
aerich init -t database.TORTOISE_ORM
aerich init-db

# Create a migration after model changes
aerich migrate --name describe_your_changes

# Apply migrations
aerich upgrade

# View migration history
aerich history
```

## Running the Application

```bash
# Start the application
python main.py
```

The API will be available at http://localhost:8001.

## API Endpoints

- `GET /users`: List all users
- `POST /users`: Create a new user
- `GET /users/{user_id}`: Get a specific user
- `PUT /users/{user_id}`: Update a user
- `DELETE /users/{user_id}`: Delete a user
- `GET /todos`: List all todos
- `POST /todos`: Create a new todo
- `GET /todos/{todo_id}`: Get a specific todo
- `PUT /todos/{todo_id}`: Update a todo
- `DELETE /todos/{todo_id}`: Delete a todo 