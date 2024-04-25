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

from keyboards.inline.mane_kb import main_menu
from states.answer_state import topic_choice
from keyboards.inline.mane_kb import main_menu, request_btn, back_keyboard, confirm_keyboard

from keyboards.default.base_kb import new_request_btn, end_request_btn
from aiogram.dispatcher.filters import ChatTypeFilter


# Пользователь может отправить несклько сообщений, надо быть готовыми это принять,
#  поэтому вводим дополнительню кнопку согласия


async def take_state_data(state):
    data = await state.get_data()
    return data['n']


def convert_to_album(message):
    pass


async def confirm_sending(message):
    await message.answer("Правила публикации сообщения", reply_markup=confirm_keyboard())


######### Прием фото/видео/альбома
@dp.message_handler(ChatTypeFilter(chat_type='private'), state=topic_choice.media_choice, is_media_group=True,
                    content_types=['photo', 'video'])
async def take_answer_with_media_group(message: types.Message, album: List[types.Message], state: FSMContext):
    print('I AM IN take_answer_with_media_group')

    # записываем аналитику
    stat = await state.get_state()
    info = analys.parse_message(message, stat)
    await write.write_in(info)

    photo_ids = []
    for obj in album:
        if obj.photo:
            ph = obj.photo[-1]
            photo_ids.append(types.InputMediaPhoto(ph.file_id))
        else:
            video_id = obj[obj.content_type].file_id
            photo_ids.append(types.InputMediaVideo(video_id))

    async with state.proxy() as data:
        data['msg'].extend(photo_ids)
        data['caption'] = None
        data['n'] += len(photo_ids)

    n = await take_state_data(state)
    try:
        await bot.delete_message(message.chat.id, message.message_id - 1)
    except:
        pass
    # if n >= 5:
    #     await message.answer()
    await message.answer('pass', reply_markup=request_btn())
    # await bot.send_media_group(message.chat.id, photo_ids)

    # await message.answer(txt.answer_confirm_text, reply_markup=new_request_btn())
    # await state.finish()


@dp.message_handler(ChatTypeFilter(chat_type='private'), state=topic_choice.media_choice,
                    content_types=types.ContentTypes.PHOTO)
async def take_answer_with_photo(message: types.Message, state: FSMContext):
    print("##########I AM IN take_answer_with_photo")
    print(message.photo[-1].file_id)
    # записываем аналитику
    stat = await state.get_state()
    info = analys.parse_message(message, stat)
    await write.write_in(info)

    photo_id = message.photo[-1].file_id
    caption = message.caption

    async with state.proxy() as data:
        data['msg'].append(types.InputMediaPhoto(photo_id))
        data['caption'] = caption
        data['n'] += 1

    n = await take_state_data(state)
    try:
        await bot.delete_message(message.chat.id, message.message_id - 1)
    except Exception:
        print('HAVNT DELETED')
    await message.answer(txt.media_choice_text(n), reply_markup=request_btn())


@dp.message_handler(ChatTypeFilter(chat_type='private'), state=topic_choice.media_choice,
                    content_types=['video'])
async def take_answer_with_video(message: types.Message, state: FSMContext):
    print("##########I AM IN take_answer_with_video")
    print(message)

    # записываем аналитику
    stat = await state.get_state()
    info = analys.parse_message(message, stat)
    await write.write_in(info)

    video_id = message.video.file_id
    caption = message.caption

    async with state.proxy() as data:
        data['msg'].append(types.InputMediaVideo(video_id))
        data['caption'] = caption
        data['n'] += 1

    n = await take_state_data(state)
    try:
        await bot.delete_message(message.chat.id, message.message_id - 1)
    except:
        print('HAVNT DELETED')
        pass
    await message.answer(txt.media_choice_text(), reply_markup=request_btn())


@dp.callback_query_handler(ChatTypeFilter(chat_type='private'), state=topic_choice.media_choice, text='next_step')
async def take_text_description(call: CallbackQuery, state: FSMContext):
    n = await take_state_data(state)
    await call.message.edit_text(txt.text_choice_text(), reply_markup=back_keyboard())
    await topic_choice.text_handle.set()


########### Конец приема медиа
@dp.message_handler(ChatTypeFilter(chat_type='private'), state=topic_choice.text_handle)
async def confirm_info(message: types.Message, state: FSMContext):
    await message.answer('Ваш запрос:')
    text = message.text
    async with state.proxy() as data:
        data['text'] = text

    data = await state.get_data()
    media_id = data['msg']
    n = data['n']
    if n == 0:
        await message.answer(text)
    else:
        media_id[0].caption = text
        await bot.send_media_group(message.chat.id, media_id)

    # await message.answer(txt.confirm_sending_request(), reply_markup=confirm_keyboard())
    await bot.send_message(message.chat.id, txt.confirm_request_text(), reply_markup=confirm_keyboard(),
                           reply_to_message_id=message.message_id + 2, disable_web_page_preview=True)
    await topic_choice.confirm.set()


@dp.callback_query_handler(ChatTypeFilter(chat_type='private'), state=topic_choice.confirm, text='send_request')
async def send_request(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(txt.success_text())

    data = await state.get_data()
    media_id = data['msg']
    text = data['text']
    n = data['n']
    if n == 0:
        await bot.send_message(channel_id, text)
    else:
        media_id[0].caption = text
        await bot.send_media_group(channel_id, media_id)

    await state.finish()
