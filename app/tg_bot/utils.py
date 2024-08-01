from aiogram.types import Message

from app.models import BotsUser


async def build_user_from_message(message: Message) -> BotsUser:
    return BotsUser(
        chat_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        phone=message.contact.phone_number if message.contact else None
    )
