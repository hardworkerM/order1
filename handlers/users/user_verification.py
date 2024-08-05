import asyncio

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, channel_id, admin_chat_id
from typing import List, Union
from aiogram.types import CallbackQuery

from aiogram.dispatcher import FSMContext

from help_functions.sql import user as u
from help_functions.sql import analytics as analys
from help_functions.file_work import write
import message_texts.texts as txt
import message_texts.warning_text as warning_text

from states.answer_state import topic_choice
from states.new_user_state import new_user
from keyboards.default.base_kb import new_request_btn, end_request_btn
from keyboards.inline.channel_kb import new_user_accept_keyboard
from keyboards.inline.mane_kb import main_menu, request_btn, back_keyboard, topic_lvl1_kb
from keyboards.inline.confirm_kb import verification_done, verification_failed
from aiogram.dispatcher.filters import ChatTypeFilter

"""
НОВЫЙ ПОЛЬЗОВАТЛЬ
"""


@dp.message_handler(ChatTypeFilter(chat_type='private'), state=new_user.home)
async def new_user_wait(message: types.Message, state: FSMContext):
    house = message.text
    async with state.proxy() as data:
        data['address'] = house
    await message.answer('Пришлите фотографию из окна или кватанцию ЖКУ')
    await new_user.got_photo.set()


@dp.message_handler(ChatTypeFilter(chat_type='private'), state=new_user.got_photo, content_types=['photo'])
async def new_user_wait(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_alias = message.from_user.username
    data = await state.get_data()
    address = data['address']

    await bot.send_photo(admin_chat_id, message.photo[-1].file_id,
                         caption=txt.admin_confirm_photo_text(address, user_id, user_alias),
                         reply_markup=new_user_accept_keyboard(message.chat.id))
    await message.answer('Большое спасибо!\nАдминистрации ответит как можно скорее!')
    await new_user.confirm.set()


@dp.message_handler(ChatTypeFilter(chat_type='private'), state=new_user.confirm)
async def new_user_wait(message: types.Message, state: FSMContext):
    await message.answer('Пожалуйста, подождите!')


@dp.callback_query_handler(ChatTypeFilter(chat_type='private'), text='try_again', state=new_user.confirm)
async def verification_again(call: CallbackQuery, state: FSMContext):
    await call.message.answer(warning_text.new_user_text())
    await new_user.home.set()
    await call.message.answer('Пришлите номер дома')

"""ПОЛЬЗОВАТЕЛЬ ПОДТВЕРЖДЕН"""


@dp.callback_query_handler(ChatTypeFilter(chat_type='private'), text='verified', state=new_user.confirm)
async def start_user_msg(call: CallbackQuery, state: FSMContext):
    await call.message.answer(txt.start_text(), reply_markup=main_menu())
    await state.finish()


""" РЕАКЦИЯ АДМИНОВ"""


@dp.callback_query_handler(lambda x: x.data.split('_')[0] == 'user')
async def make_decision_for_user(call: CallbackQuery, state: FSMContext):
    from_user = call.from_user.id

    info = call.data.split('_')
    result = info[1]
    chat_id = info[2]

    data = call.message.caption.split(': ')[1:]
    alias = data[0].split('\n')[0]
    user_id = data[1].split('\n')[0]
    house = data[2].split('\n')[0]

    if result == 'accept':
        await bot.send_message(chat_id, txt.confirm_user_success(), reply_markup=verification_done())
        u.update_user_verification(chat_id)
    else:
        await bot.send_message(chat_id, txt.confirm_user_fail(), reply_markup=verification_failed())
    publish_text = txt.admin_confirm_user_result(result, int(user_id), alias, house)

    await call.message.edit_caption(publish_text)
    await state.finish()
    # НУЖНО ЗАПИСАТЬ В БД И ИЗМЕНИТЬ СОСТОЯНИЕ
