from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user_follows" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "follower_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    "following_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "user_follows";"""
