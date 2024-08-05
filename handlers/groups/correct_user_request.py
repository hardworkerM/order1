from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, channel_id, admin_chat_id
from aiogram import types

from typing import List, Union
from aiogram.types import CallbackQuery

from aiogram.dispatcher import FSMContext

from help_functions.sql import user as u
from help_functions.sql import analytics as analys
from help_functions.file_work import write
import message_texts.warning_text as warning_txt
import message_texts.texts as txt
from keyboards.inline.mane_kb import main_menu, request_btn, back_keyboard, topic_lvl1_kb, topic_lvl2_kb
from help_functions.sql import tasks as tas

from states.answer_state import topic_choice_admin
from keyboards.inline.mane_kb import main_menu, request_btn, back_keyboard, confirm_keyboard
from keyboards.inline.channel_kb import admin_keyboard

from keyboards.default.base_kb import new_request_btn, end_request_btn
from aiogram.dispatcher.filters import ChatTypeFilter


async def get_topics(state):
    data = await state.get_data()

    lvl1 = data['topic_lvl1']
    lvl2 = data['topic_lvl2']

    return lvl1, lvl2


@dp.callback_query_handler(lambda x: x.data.split(';')[0]=='change_user_info')
async def change_request(call: CallbackQuery, state: FSMContext):
    await topic_choice_admin.lvl1.set()
    plus_info = call.data.split(';')
    order_id = plus_info[1]
    user_id = plus_info[2]
    async with state.proxy() as data:
        data['order_id'] = order_id
        data['user_id'] = user_id

    text = call.message.text
    print(text)
    await call.message.answer(f'Давайте исправим объявление от {user_id}',
                              reply_markup=topic_lvl1_kb())


@dp.callback_query_handler(state=topic_choice_admin.all_states, text='back')
async def end_request(call: CallbackQuery, state: FSMContext):
    msg_id = call.message.message_id
    await call.answer('Отменяю редактирование')
    await bot.delete_message(call.message.chat.id, msg_id)
    await state.finish()


@dp.callback_query_handler(state=topic_choice_admin.lvl1)
async def change_lvl1(call: CallbackQuery, state: FSMContext):
    topic_lvl1 = call.data

    await topic_choice_admin.lvl2.set()
    if topic_lvl1 not in ['Найдено', 'Потеряно']:
        msg_id = await call.message.edit_text(txt.topic_lvl2_text(topic_lvl1), reply_markup=topic_lvl2_kb(topic_lvl1))
    else:
        msg_id = await send_request(call, state)
    async with state.proxy() as data:
        data['topic_lvl1'] = topic_lvl1
        data['msg_id'] = msg_id.message_id


def transfer_media(info):
    file_id, str_type = info
    if str_type == 'photo':
        return types.InputMediaPhoto(file_id)
    return types.InputMediaVideo(file_id)


@dp.callback_query_handler(state=topic_choice_admin.lvl2)
async def send_request(call: CallbackQuery, state: FSMContext):
    topic_lvl2 = call.data

    async with state.proxy() as data:
        data['topic_lvl2'] = topic_lvl2

    topic_lvl1, topic_lvl2 = await get_topics(state)

    data = await state.get_data()
    user_id = data['user_id']
    order_id = data['order_id']
    msg_id = data['msg_id']
    # print(msg_id)
    await bot.delete_message(call.message.chat.id, msg_id)

    user_info = tas.find_user_info(user_id)
    user_alias = user_info[0]
    first_name = user_info[1]

    order_info = tas.find_order_info(user_id, order_id)
    user_id = order_info[1]
    medias = order_info[2]
    text = order_info[3]

    text_to_publish = txt.add_meta_data_to_text(text, topic_lvl1, topic_lvl2, user_id, user_alias, first_name)

    order_id = tas.make_order_id()

    tas.new_request(order_id, user_id, medias, text, topic_lvl1, topic_lvl2)

    if medias == 'None':
        sent_message = await bot.send_message(admin_chat_id, text_to_publish,
                                              reply_markup=admin_keyboard(order_id, user_id, ))
    else:
        media_group = [transfer_media(media_info.split(':')) for media_info in medias.split(';')]
        media_group[0].caption = text_to_publish

        sent_messages = await bot.send_media_group(admin_chat_id, media_group)
        await bot.send_message(admin_chat_id,
                               'Подтвердить?',
                               reply_markup=admin_keyboard(order_id, user_id),
                               reply_to_message_id=sent_messages[0].message_id)
    await state.finish()
        # await bot.send_message(admin_chat_id, text, reply_markup=admin_keyboard(have_more=1, msg_id=msg_id))
