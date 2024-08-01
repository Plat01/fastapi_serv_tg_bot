from aiogram import Router
from aiogram.filters import CommandStart

from .handlers import start, echo


start_handler_filters = CommandStart()
def prepare_router() -> Router:
    """
    prepare routing
    """
    user_router = Router()
    user_router.message.register(start.start_handler, start_handler_filters)
    user_router.message.register(echo.echo_handler)

    return user_router

