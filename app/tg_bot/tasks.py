from . import bot
from ..config import settings


async def send_message_to_admin(txt: str):
    await bot.send_message(
        chat_id=settings.NOTIFICATION_ID,
        text=txt
    )
