from tortoise import Tortoise


TORTOISE_ORM = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        },
    },
}


async def init_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["models"]},
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
