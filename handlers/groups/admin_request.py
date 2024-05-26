from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, channel_id, admin_chat_id

from typing import List, Union
from aiogram.types import CallbackQuery

from aiogram.dispatcher import FSMContext

from help_functions.sql import user as u
from help_functions.sql import analytics as analys
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
    from_user = call.from_user.id
    # МОЖЕТ СЮДА ВШИТЬ id сообщения и передавать в кнопку
    await bot.send_message(from_user,call.message.text + '\n\n' + warning_txt.was_declined_text())
    info = await bot.get_chat(call.message.chat.id)
    print(call)
    await call.message.edit_text(call.message.text + "'\n\nОТКЛОНЕНО")


@dp.callback_query_handler(lambda x: x.data.split(';')[0]=='send_in_channel')
async def decline_sending(call: CallbackQuery, state: FSMContext):
    one_more = call.data.split(';')[-1]
    from_user = call.from_user.id
    msg_id = call.message.message_id
    chat_id = call.message.chat.id
    if one_more == '1':
        await bot.copy_message(channel_id, chat_id, msg_id-1)

    mg_id = await bot.copy_message(channel_id, chat_id, msg_id)

    await bot.send_message(from_user, txt.success_admin_accept_text(mg_id.message_id))
    await call.message.edit_text(call.message.text + warning_txt.was_approved_text(mg_id.message_id))


