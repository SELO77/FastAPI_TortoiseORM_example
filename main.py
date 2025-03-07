from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from controller import router
from database import TORTOISE_ORM

app = FastAPI(title="FastAPI Tortoise ORM Example")

# Include the router
app.include_router(router)

# Register Tortoise ORM
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # Disable auto schema generation, we'll use Aerich
    add_exception_handlers=True,
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
