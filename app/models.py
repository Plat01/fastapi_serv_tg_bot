import typing
from pydantic import BaseModel, Field, EmailStr

from aiogram.types.message import Message
from sqlmodel import SQLModel


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


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    items: list["Item"] = Relationship(back_populates="owner")

