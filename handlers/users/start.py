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
from aiogram.dispatcher.filters import ChatTypeFilter
from filters import TimeFilter


async def fill_info_about_user(message: types.Message):
    user_id = message.chat.id
    alias = message.from_user.username
    name = message.from_user.full_name
    print(user_id, alias, name)
    if not u.check_user(user_id):
        u.main_info_fill(user_id, alias, name)


@dp.message_handler(ChatTypeFilter(chat_type='private'), CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    """
    Хендел для /start
    Проверяется есть ли юзер в бд
    Возвращает текст меню, ловится со всего
    """
    #
    # ph_id = 'AgACAgIAAxkBAAIGBmavacOpMDUi5PDNDYE0-KPoCMWtAALv3TEbXESBSfmFBBfVdiX7AQADAgADeQADNQQ'
    # ph_id_2 = 'AgACAgIAAxkBAAIGB2avacMsI1F29KtnG-Da03UhRze5AALw3TEbXESBSYmIAAE4AAFys9kBAAMCAAN5AAM1BA'
    # ph = [ph_id_2, ph_id]
    # media_id = [types.InputMediaPhoto(i) for i in ph]
    # media_id[0].caption = 'ОПАААА ШЛЮХИ'
    # print(media_id)
    # await bot.send_media_group(admin_chat_id, media_id)
    #
    # await bot.send_photo(admin_chat_id, ph_id)


    await fill_info_about_user(message)
    user_id = message.chat.id
    # записываем аналитику
    try:
        await bot.delete_message(message.chat.id, message.message_id-1)
    except:
        pass
    finally:
        await message.answer(txt.start_text(), reply_markup=main_menu())


"""
Блок НОВЫЙ ЗАПРОС - вступить в него и закончить его
"""


@dp.callback_query_handler(ChatTypeFilter(chat_type='private'), text="new_request")
async def prepare_answer(call: CallbackQuery, state: FSMContext, ):
    user_id = call.message.chat.id

    is_verified = u.check_user_verified(user_id)
    if is_verified:
        await call.message.edit_text(txt.topic_lvl1_text(), reply_markup=topic_lvl1_kb())
        await topic_choice.lvl1.set()

    else:
        await call.message.answer(warning_text.new_user_text())
        await new_user.home.set()
        await call.message.answer('Пришлите номер дома')


# Закончить общение
@dp.callback_query_handler(ChatTypeFilter(chat_type='private'), state='*', text='back')
async def end_request(call: CallbackQuery, state: FSMContext):
    # записываем аналитику
    stat = await state.get_state()

    # answer_st:confirm_request
    if stat == 'answer_st:confirm_request':
        try:
            await bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        finally:
            await call.answer('Отменили формирование')
            await call.message.answer(txt.start_text(), reply_markup=main_menu())
    else:
        await call.message.edit_text(txt.start_text(), reply_markup=main_menu())

    await state.finish()

