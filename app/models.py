import typing
from pydantic import BaseModel, Field

from aiogram.types.message import Message


class BotsUser(BaseModel):
    """
    pydantic base model for User
    """
    chat_id: int
    first_name: typing.Optional[str]
    username: typing.Optional[str]
    last_name: typing.Optional[str]
    phone: typing.Optional[str] = Field(default=None, max_length=16)
    latitude: typing.Optional[float] = Field(default=None)
    longitude: typing.Optional[float] = Field(default=None)


async def build_user(message: Message) -> BotsUser:
    return BotsUser(
        chat_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        phone=message.contact.phone_number if message.contact else None
    )
