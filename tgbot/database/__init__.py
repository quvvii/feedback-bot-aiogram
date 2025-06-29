from tortoise import Tortoise
from config import Config


config = Config()


async def connect_database():
    await Tortoise.init(
        db_url=config.DB_URL,
        modules={
            'models': ['tgbot.database.models'],
        }
    )

    await Tortoise.generate_schemas()


async def close_connection():
    await Tortoise.close_connections()
