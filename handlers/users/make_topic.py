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


async def get_topics(state):
    data = await state.get_data()

    lvl1 = data['topic_lvl1']
    lvl2 = data['topic_lvl2']

    return lvl1, lvl2


@dp.callback_query_handler(ChatTypeFilter(chat_type='private'), state=topic_choice.lvl1)
async def send_request(call: CallbackQuery, state: FSMContext):
    topic_lvl1 = call.data

    async with state.proxy() as data:
        data['topic_lvl1'] = topic_lvl1

    await topic_choice.lvl2.set()
    if topic_lvl1 not in ['Найдено', 'Потеряно']:
        await call.message.edit_text(txt.topic_lvl2_text(topic_lvl1), reply_markup=topic_lvl2_kb(topic_lvl1))
    else:
        await send_request(call, state)


@dp.callback_query_handler(ChatTypeFilter(chat_type='private'), state=topic_choice.lvl2)
async def send_request(call: CallbackQuery, state: FSMContext):
    topic_lvl2 = call.data

    async with state.proxy() as data:
        data['topic_lvl2'] = topic_lvl2
        # Инициилизируем
        data['msg'] = []
        data['content_types'] = []
        data['caption'] = ''
        data['type'] = ''
        data['n'] = 0

    lvl1, lvl2 = await get_topics(state)
    await call.message.edit_text(txt.media_choice_text(lvl1, lvl2),
                                 reply_markup=request_btn())

    await topic_choice.media_choice.set()
