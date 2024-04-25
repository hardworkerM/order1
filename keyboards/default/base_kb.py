from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def new_request_btn():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Новый запрос")
    kb.add(button1)

    return kb


def end_request_btn():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Отменить")
    kb.add(button1)

    return kb