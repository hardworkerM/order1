import asyncio

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, channel_id
from typing import List, Union
from aiogram.types import CallbackQuery

from aiogram.dispatcher import FSMContext

from help_functions.sql import user as u
from help_functions.sql import analytics as analys
from help_functions.file_work import write
import message_texts.texts as txt

from states.answer_state import topic_choice
from keyboards.default.base_kb import new_request_btn, end_request_btn
from keyboards.inline.mane_kb import main_menu, request_btn, back_keyboard, topic_lvl1_kb
from aiogram.dispatcher.filters import ChatTypeFilter


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    """
    Хендел для /start
    Проверяется есть ли юзер в бд
    Возвращает текст меню, ловится со всего
    """
    print(message)