from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, bot
from aiogram.types import InputFile
from pathlib import Path
import os
from help_functions.load_db import check_data


@dp.message_handler(commands='info')
async def bot_info(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/info - Получить справку",
            "/help - Напиши нам если что-то произошло")
    
    await message.answer("\n".join(text))


@dp.message_handler(text='db')
async def send_db(message: types.Message):
    print('I AM IN SEND_DB')
    d = os.getcwd()
    print(d)
    ### нужно все записать
    await check_data.load_db_info()
    path = d + '\\data\\databases.db'
    file = open(path, 'rb')
    # await message.answer_document(path)
    await bot.send_document(565843474, file)
    # await message.answer_document(file)
    file.close()