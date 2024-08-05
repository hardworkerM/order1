from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from aiogram.dispatcher.filters import ChatTypeFilter
import message_texts.texts as txt
import message_texts.warning_text as w_txt
from keyboards.default.base_kb import new_request_btn, end_request_btn
from keyboards.inline.mane_kb import main_menu, request_btn, confirm_keyboard

# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием


async def make_answer_by_state(message, state):
    if not state:
        await message.answer(txt.start_text(), reply_markup=main_menu())
    elif state == 'topic_choice:media_choice':
        await message.answer(w_txt.txt_but_need_media(), reply_markup=request_btn())
    elif state == 'answer_st:confirm_request':
        await message.answer(txt.confirm_sending_request(), reply_markup=confirm_keyboard())
    elif state=='new_user:confirm':
        await message.answer('Пожалуйста, дождитесь процесса верификации, это занимает меньше дня')
    elif state=='new_user:got_photo':
        await message.answer('Отправьте именно фотографию!\nПришлите фотографию из окна или кватанцию ЖКУ')
    elif state=='new_user:home':
        await message.answer('Напишите текстом номер дома')


@dp.message_handler(ChatTypeFilter(chat_type='private'), state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    print(message)
    print('ECHO state')
    status = await state.get_state()
    print(status, type(status))
    try:
        await bot.delete_message(message.chat.id, message.message_id-1)
    except:
        pass
    finally:
        await make_answer_by_state(message, status)
