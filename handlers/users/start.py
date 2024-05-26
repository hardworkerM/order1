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


@dp.message_handler(ChatTypeFilter(chat_type='private'), CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    """
    Хендел для /start
    Проверяется есть ли юзер в бд
    Возвращает текст меню, ловится со всего
    """
    user_id = message.chat.id
    # ПРОВЕРКА НА ТО ЧТО ПОЛЬЗОВАТЕЛЬ В
    user_is_new = 1 # СДЕЛАТЬ!

    if user_is_new==1:
    # записываем аналитику
        try:
            await bot.delete_message(message.chat.id, message.message_id-1)
        except:
            pass
        finally:
            await message.answer(txt.start_text(), reply_markup=main_menu())

    else:
        await message.answer(warning_text.new_user_text())
        await new_user.home.set()
        await message.answer('Пришлите номер дома')


"""
Блок НОВЫЙ ЗАПРОС - вступить в него и закончить его
"""


@dp.callback_query_handler(ChatTypeFilter(chat_type='private'), text="new_request")
async def prepare_answer(call: CallbackQuery, state: FSMContext, ):
    await call.message.edit_text(txt.topic_lvl1_text(), reply_markup=topic_lvl1_kb())
    await topic_choice.lvl1.set()


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
    data = await state.get_data()
    address = data['address']

    await bot.send_photo(admin_chat_id, message.photo[-1].file_id,
                         caption=txt.admin_confirm_photo_text(address, user_id),
                         reply_markup=new_user_accept_keyboard(message.chat.id))
    await message.answer('Большое спасибо за понимание!\nАдминистрации ответит как можно скорее!>')


