from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from tgbot.keyboards.reply import *

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("Вы играете в ксго?", reply_markup=start.as_markup(resize_keyboard=True))