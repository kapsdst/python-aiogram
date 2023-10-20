from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from tgbot.keyboards.reply import *
from tgbot.keyboards.inline import *
from aiogram import F
from random import randint


user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("Здравствуйте, выберите файл", reply_markup=start.as_markup(resize_keyboard=True))





@user_router.callback_query(F.data == "1")
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer_sticker(sticker="CAACAgIAAxkBAAEKkARlMrAILXyvWJdfpAFyGzbYQxWXxQACTyAAAl2maErMNZObhmRn_zAE")

@user_router.callback_query(F.data == "2")
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer_sticker(sticker="CAACAgIAAxkBAAEKkBhlMrQYD3P5YvA4Mdr4WmC69wh-EwACAhUAAoB8oUiebai-kHZhHjAE")

@user_router.callback_query(F.data == "3")
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer_sticker(sticker="CAACAgIAAxkBAAEKkB9lMrjPtWzKy2UMsxiMbsTu5wgMvwAC6QsAAubGoUj1k_7LEVr8_jAE")

@user_router.callback_query(F.data == "4")
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer_sticker(sticker="CAACAgIAAxkBAAEKkCFlMrlo1mDRw_lNWm-D_IKMdL2ArgAC1icAAiIxmEo2zjSsXH_DcTAE")

@user_router.callback_query(F.data == "5")
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer_sticker(sticker="CAACAgIAAxkBAAEKkCNlMrnz0S2z27TYAAE7gWj9rKOPJz0AAkADAAK1cdoGuRLw3B1VGFwwBA")