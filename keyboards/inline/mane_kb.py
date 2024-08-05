from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from message_texts import texts as txt



def back_btn():
    back = InlineKeyboardButton("X Отмена", callback_data='back')

    return back


def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)

    btn1 = InlineKeyboardButton("Добавить объявление", callback_data='new_request')

    btn2 = InlineKeyboardButton("Доска объявлений",
                                url='https://t.me/upskolkovosale',)
    btn3 = InlineKeyboardButton("Чаты домов",
                                url='https://telegra.ph/CHaty-domov-01-11')
    btn4 = InlineKeyboardButton("Услуги от соседей",
                                url='https://t.me/madeinUpSkolkovo')
    btn5 = InlineKeyboardButton("Чаты по темам",
                                url='https://telegra.ph/CHaty-01-22-2')
    btn6 = InlineKeyboardButton("Справочник",
                                url='https://telegra.ph/Spravochnik-nashego-ZHK-01-11-2')
    btn7 = InlineKeyboardButton("Правила",
                                url='https://telegra.ph/Pravila-03-01-6')
    btn8 = InlineKeyboardButton("Реклама",
                                url='https://t.me/UpSkolkovoHelpBot')
    btn9 = InlineKeyboardButton("Служба поддержки (ошибки предложени и прочее)", url='https://t.me/UpSkolkovoHelpBot')


    markup.row(btn1)
    markup.add(btn2, btn3)
    markup.add(btn4, btn5)
    markup.add(btn6, btn7)
    markup.row(btn8)
    markup.row(btn9)

    return markup


def topic_lvl1_kb():
    markup = InlineKeyboardMarkup(row_width=1)

    topic_list = txt.topic_list_1()

    for topic in topic_list:
        btn = InlineKeyboardButton(topic, callback_data=topic)
        markup.row(btn)
    markup.row(back_btn())
    return markup


def topic_lvl2_kb(topic):
    markup = InlineKeyboardMarkup(row_width=1)

    topic_list2 = txt.topic_list_1(topic)
    for topic2 in topic_list2:
        btn = InlineKeyboardButton(topic2, callback_data=topic2)
        markup.row(btn)
    markup.row(back_btn())
    return markup


def request_btn():
    markup = InlineKeyboardMarkup(row_width=1)

    btn1 = InlineKeyboardButton("Далее", callback_data='next_step')

    markup.row(btn1)
    markup.row(back_btn())

    return markup


def confirm_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)

    btn1 = InlineKeyboardButton("Подтвердить бесплатное размещение", callback_data='send_request')
    btn2 = InlineKeyboardButton("Платное объявление", callback_data='advert')

    markup.row(btn1)
    markup.row(btn2)
    markup.row(back_btn())

    return markup


def back_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(back_btn())

    return markup