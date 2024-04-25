from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from aiogram.dispatcher.filters import ChatTypeFilter
import message_texts.texts as txt
from keyboards.default.base_kb import new_request_btn, end_request_btn
from keyboards.inline.mane_kb import main_menu, request_btn, confirm_keyboard

# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием


async def make_answer_by_state(message, state):
    if not state:
        await message.answer(txt.start_text(), reply_markup=main_menu())
    elif state == 'answer_st:take_request':
        await message.answer(txt.answer_help_text2(), reply_markup=request_btn())
    elif state == 'answer_st:confirm_request':
        await message.answer(txt.confirm_sending_request(), reply_markup=confirm_keyboard())


@dp.message_handler(ChatTypeFilter(chat_type='private'), state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    print('ECHO state')
    print(message.text)
    status = await state.get_state()
    print(status, type(status))
    try:
        await bot.delete_message(message.chat.id, message.message_id-1)
    except:
        pass
    finally:
        await make_answer_by_state(message, status)
