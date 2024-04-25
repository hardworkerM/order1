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

from keyboards.inline.mane_kb import topic_lvl2_kb
from states.answer_state import topic_choice
from keyboards.inline.mane_kb import main_menu, request_btn, back_keyboard, confirm_keyboard

from keyboards.default.base_kb import new_request_btn, end_request_btn
from aiogram.dispatcher.filters import ChatTypeFilter


@dp.callback_query_handler(ChatTypeFilter(chat_type='private'), state=topic_choice.lvl1)
async def send_request(call: CallbackQuery, state: FSMContext):
    topic = call.message.text
    print(call.data)
    print(topic)
    await call.message.edit_text(txt.topic_lvl2_text(call.data),
                                 reply_markup=topic_lvl2_kb(call.data))

    await topic_choice.lvl2.set()


@dp.callback_query_handler(ChatTypeFilter(chat_type='private'), state=topic_choice.lvl2)
async def send_request(call: CallbackQuery, state: FSMContext):
    topic = call.message.text
    print(topic)
    await call.message.edit_text(txt.media_choice_text(),
                                 reply_markup=request_btn())

    await topic_choice.media_choice.set()