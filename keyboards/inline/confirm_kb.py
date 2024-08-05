from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from message_texts import texts as txt


def request_btns():

    markup = InlineKeyboardMarkup()
    confirm = InlineKeyboardButton(text='Готово', callback_data='ok')
    reload = InlineKeyboardButton(text='Заново', callback_data='no')
    cancel = InlineKeyboardButton(text='Уйти', callback_data='out')
    markup.row(confirm, reload, cancel)

    return markup


def verification_done():

    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text='Приступить', callback_data='verified')
    markup.row(btn)

    return markup


def verification_failed():

    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text='Отправить еще раз', callback_data='try_again')
    markup.row(btn)

    return markup

