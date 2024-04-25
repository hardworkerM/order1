def start_text():
    start_text = "Чем я могу вам помочь?"
    return start_text


def stop_topics():
    t = 'Не размещаем: аптека, курение, алкоголь.'
    return t


def topic_list_2():
    topics = ['Одежда, обувь и аксессуары',
     'Детское',
     'Красота и здоровье',
     'Спорт и хобби',
     'Дом и дача',
     'Техника',
     'Недвижимость',
     'Транспорт',
     'Работа',
     'Животные'
     ]
    return topics


def topic_list_1(key=None):
    topics = topic_list_2()
    d = {
        'Куплю': topics,
        'Продам': topics,
        'Сдам': topics,
        'Сниму': topics,
        'Вакансия': topics,
        'Резюме': topics,
        'Отдам': topics,
        'Приму в дар': topics,
        'Найдено': 0,
        'Потеряно': 0,

    }
    if key:
        return d[key]
    return d


def topic_lvl1_text():
    text = '<b>Добавление объявления</b>\n\nВыберите категорию:'

    return text


def topic_lvl2_text(lvl1):
    text = f'<b>Добавление объявления</b>\n\nКатегорию: {lvl1}'
    warn = f'<i>{stop_topics()}</i>'
    return f'{text}\n\n{warn}'


def media_choice_text():
    text = 'Выборк меди, отправьте медиа'

    return text


def text_choice_text():
    text = 'Введи текст сообщения'

    return text


def confirm_request_text():
    text = 'Отправляем, братик?'

    return text


def success_text():
    text = 'Оправлено!'
    return text