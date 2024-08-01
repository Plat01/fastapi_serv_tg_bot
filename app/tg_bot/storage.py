from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis

from ..config import settings

storage = RedisStorage(
    redis=Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DATABASE
    )
)