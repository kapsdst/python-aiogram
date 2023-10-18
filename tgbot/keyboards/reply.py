from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start = ReplyKeyboardBuilder()
start.add(
    KeyboardButton(text="jopa"),
    KeyboardButton(text="да(я педик)"),
    KeyboardButton(text="нет(я натурал)")
)
