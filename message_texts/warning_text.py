from message_texts.texts import media_choice_text

def txt_but_need_media():
    t = media_choice_text()
    t2 = "\n<b>Отправьте только фото / видео, если хотите ввести текст - нажмите Далее\n</b>"
    return t2+t


def request_denied_text():
    text = "Ваше объявление было отклонено\n" \
           " Повторно ознакомьтесь с <a href='https://telegra.ph/Pravila-03-01-6https://telegra.ph/Pravila-03-01-6'>правилами</a>" \
           " или свяжитесь с поддержкой через бота @UpSkolkovoHelpBot."

    return text


def new_user_text():
    t = 'Вы размещаете объявление в первый раз\n' \
        'Необходимо подтвердить, что Вы из нашего ЖК Сколковский (как вариант, из Трехгорки).\n' \
        'Напишите номер дома и пришлите фото из окна или квитанцию ЖКУ, после этого мы можем подтвердить размещение объявления.'

    return t


def was_declined_text():
    text = '\n\n Объявление отклонено из-за нарушения правил.  ' \
           'Повторно ознакомьтесь с ' \
           '<a href="https://telegra.ph/Pravila-03-01-6">правилами</a>'
    return text


def was_approved_text(msg_id):
    text = f'\n\nСообщение было отправлено: https://t.me/c/2129475388/{msg_id}'

    return text