from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

builder = InlineKeyboardBuilder()
builder.add(InlineKeyboardButton(
    text="Нажми меня",
    callback_data="random_value")
)