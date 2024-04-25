from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def request_btns():

    markup = InlineKeyboardMarkup()
    confirm = InlineKeyboardButton(text='Готово', callback_data='ok')
    reload = InlineKeyboardButton(text='Заново', callback_data='no')
    cancel = InlineKeyboardButton(text='Уйти', callback_data='out')
    markup.row(confirm, reload, cancel)

    return markup
