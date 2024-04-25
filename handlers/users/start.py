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


@dp.message_handler(ChatTypeFilter(chat_type='private'), CommandStart())
async def bot_start(message: types.Message):
    """
    Хендел для /start
    Проверяется есть ли юзер в бд
    Возвращает текст меню, ловится со всего
    """
    # записываем аналитику
    info = analys.parse_message(message)
    await write.write_in(info)
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
    await call.message.edit_text(txt.topic_lvl1_text(), reply_markup=topic_lvl1_kb())
    await topic_choice.lvl1.set()


# Закончить общение
@dp.callback_query_handler(ChatTypeFilter(chat_type='private'), state='*', text='back')
async def end_request(call: CallbackQuery, state: FSMContext):
    print('I AN IN end_request')
    # записываем аналитику
    stat = await state.get_state()
    info = analys.parse_message(call.message, stat if stat else 'None')
    await write.write_in(info)

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


