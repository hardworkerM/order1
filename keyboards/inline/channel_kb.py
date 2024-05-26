from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from message_texts import texts as txt



def back_btn():
    back = InlineKeyboardButton("X Отмена", callback_data='back')

    return back


def back_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(back_btn())

    return markup


def admin_keyboard(have_more=0, msg_id=None):
    markup = InlineKeyboardMarkup(row_width=2)

    btn1 = InlineKeyboardButton("Отправить", callback_data='send_in_channel'+';'+str(have_more))

    btn2 = InlineKeyboardButton("Отменить", callback_data='decline_send_in_chanel' + ';'+str(msg_id))
    # btn3 = InlineKeyboardButton("Отправить правила", callback_data='decline_send_in_chanel' + ';'+str(msg_id))


    markup.row(btn1)
    markup.row(btn2)

    return markup


def new_user_accept_keyboard(user_id):
    markup = InlineKeyboardMarkup(row_width=2)

    btn1 = InlineKeyboardButton("Принять", callback_data='user_accept'+'_'+str(user_id))

    btn2 = InlineKeyboardButton("Отклонить", callback_data='user_deny'+'_'+str(user_id))

    markup.row(btn1)
    markup.row(btn2)

    return markup