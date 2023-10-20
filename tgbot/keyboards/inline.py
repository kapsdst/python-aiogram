from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, callback_query

start = InlineKeyboardBuilder()
start.add(
    InlineKeyboardButton(text="1. Тимоха Чё ты творишь?!??!🤨",callback_data="1"),
    InlineKeyboardButton(text="2. Коты Милые🐱",callback_data="2"),
    InlineKeyboardButton(text="3. Уга буга ",callback_data="3"),
    InlineKeyboardButton(text="4. Dk pack ",callback_data="4"),
    InlineKeyboardButton(text=". Rick and Morty ",callback_data="5")
)
start.adjust(1)