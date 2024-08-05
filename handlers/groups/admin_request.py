from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, channel_id, admin_chat_id
from aiogram import types

from typing import List, Union
from aiogram.types import CallbackQuery

from aiogram.dispatcher import FSMContext

from help_functions.sql import user as u
from help_functions.sql import tasks as tas
from help_functions.file_work import write
import message_texts.warning_text as warning_txt
import message_texts.texts as txt

from states.answer_state import topic_choice
from keyboards.inline.mane_kb import main_menu, request_btn, back_keyboard, confirm_keyboard
from keyboards.inline.channel_kb import admin_keyboard

from keyboards.default.base_kb import new_request_btn, end_request_btn
from aiogram.dispatcher.filters import ChatTypeFilter


@dp.callback_query_handler(lambda x: x.data.split(';')[0]=='decline_send_in_chanel')
async def decline_sending(call: CallbackQuery, state: FSMContext):

    plus_info = call.data.split(';')
    user_id = int(plus_info[1])

    # МОЖЕТ СЮДА ВШИТЬ id сообщения и передавать в кнопку
    info_text = call.message.text
    await bot.send_message(user_id, warning_txt.was_declined_text(info_text))

    await call.message.edit_text(call.message.text + "'\n\nОТКЛОНЕНО")


def transfer_media(info):
    file_id, str_type = info
    if str_type == 'photo':
        return types.InputMediaPhoto(file_id)
    return types.InputMediaVideo(file_id)


@dp.callback_query_handler(lambda x: x.data.split(';')[0]=='send_in_channel')
async def decline_sending(call: CallbackQuery, state: FSMContext):

    plus_info = call.data.split(';')
    order_id = plus_info[1]
    user_id = int(plus_info[2])

    user_info = tas.find_user_info(user_id)
    user_alias = user_info[0]
    first_name = user_info[1]

    order_info = tas.find_order_info(user_id, order_id)
    user_id = order_info[1]
    medias = order_info[2]
    text = order_info[3]
    topic_lvl1 = order_info[4]
    topic_lvl2 = order_info[5]

    text_to_publish = txt.add_meta_data_to_text(text, topic_lvl1, topic_lvl2, user_id, user_alias, first_name)
    if medias != 'None':
        media_group = [transfer_media(media_info.split(':')) for media_info in medias.split(';')]
        media_group[0].caption = text_to_publish

        msg_info = await bot.send_media_group(channel_id, media_group)
        channel_msg_id = msg_info[0].message_id

    else:
        msg_info = await bot.send_message(channel_id, text_to_publish)
        channel_msg_id=msg_info.message_id
    # mg_id = await bot.copy_message(channel_id, chat_id, msg_id)
    # mg_id2 = await bot.copy_message(channel_id, chat_id, msg_id-1)
    # mg_id = await bot.copy_message(channel_id, chat_id, [msg_id, msg_id-1, msg_id-2])

    await bot.send_message(user_id, txt.success_admin_accept_text(channel_msg_id))
    await call.message.edit_text(call.message.text + warning_txt.was_approved_text(channel_msg_id))


