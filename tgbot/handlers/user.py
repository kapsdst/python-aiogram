from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from tgbot.keyboards.reply import *
from tgbot.keyboards.inline import *
from aiogram import F
from random import randint


user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("Вы играете в ксго?", reply_markup=start.as_markup(resize_keyboard=True))




@user_router.message(Command("random"))
async def cmd_random(message: Message):
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )

@user_router.callback_query(F.data == "random_value")
async def send_random_value(callback: Message):
    await callback.message.answer(str(randint(1, 10)))



@user_router.message(lambda message: message.text == "да(я педик)")
async def on_reply_button_click(message:Message):

    await message.answer("Да Шёл ты нахуй!")



@user_router.message(lambda message: message.text == "(я натурал)")
async def on_reply_button_click(message:Message):

    await message.answer("Да Шёл ты нахуй")