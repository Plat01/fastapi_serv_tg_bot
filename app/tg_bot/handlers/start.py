from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.tg_bot.utils import build_user_from_message


async def start_handler(message: Message, state: FSMContext) -> None:
    """
    handler will forward receive a message back to the sender
    """
    client = await build_user_from_message(message)
    # TODO: add user to database

    await message.answer(
        text=f"Hello {client.first_name}"
    )
