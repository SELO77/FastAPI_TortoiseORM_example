from tortoise import Tortoise

# Database URL
DB_URL = "sqlite://db.sqlite3"

# Tortoise ORM configuration
TORTOISE_ORM = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "UTC",
}


async def init_db():
    await Tortoise.init(
        db_url=DB_URL,
        modules={"models": ["models"]},
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
