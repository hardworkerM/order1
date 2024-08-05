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


# @dp.callback_query_handler(lambda x: x.data.split('_')[0]=='user')
# async def make_decision_for_user(call: CallbackQuery, state: FSMContext):
#     from_user = call.from_user.id
#
#     info = call.data.split('_')
#     result = info[1]
#     chat_id = info[2]
#     if result=='accept':
#         await bot.send_message(from_user, txt.confirm_user_success())
#     else:
#         await bot.send_message(from_user, txt.confirm_user_fail())
#         u.update_user_verification(from_user)
#     # await call.message.edit_text(f'Пользователь был {result}')
#     await call.message.edit_caption(f'Пользователь был {result}')
#     # НУЖНО ЗАПИСАТЬ В БД И ИЗМЕНИТЬ СОСТОЯНИЕ