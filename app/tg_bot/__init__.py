from aiogram import Bot, Dispatcher

from ..config import settings
from .storage import storage
from .router import prepare_router

bot: Bot = Bot(token=settings.BOT_TOKEN)
dispatcher: Dispatcher = Dispatcher(storage=storage)
dispatcher.include_router(prepare_router())
