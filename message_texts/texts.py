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
    text = '<b>Добавление объявления</b>\n\nВыберите тип объявления:'

    return text


def topic_lvl2_text(lvl1):
    text = f'<b>Добавление объявления</b>\n\nТип: {lvl1}'
    warn = f'<i>{stop_topics()}</i>'
    t = '<i>Выберите категорию объявления</i>'
    return f'{text}\n\n{warn}\n\n{t}'


def media_choice_text(lvl1, lvl2):
    text = 'Выборк меди, отправьте медиа'
    t1 = f'Тип: {lvl1}'
    t2 = f'Категория: {lvl2}'
    return f'{text}\n\n{t1}\n{t2}'


def text_choice_text():
    text = 'Введите текст сообщения'

    return text


def add_meta_data_to_text(text, topic_lvl1, topic_lvl2, id, name, first_name):
    category = f'<b>Категории</b>: #{("").join(topic_lvl1.title().split())} ' \
               f'#{("").join(topic_lvl2.title().split())}'
    connect = f'<b>Связатья:</b>: @{name}(#ID{id})'

    text = f'{text}\n\n{category}\n{connect}'

    return text




def make_info(user_id, lvl1, lvl2):
    pass


def confirm_request_text():
    text = 'Нажмите кнопку <b>Подтвердить бесплатное размещение</b>, если:\n' \
           '1.  Вы частное лицо (не магазин, не коммерция) \n' \
           '2. В объявлении не алкоголь, не медикаменты (в том числе витамины и БАДы), не табак (кальяны, электронные сигареты).\n' \
           '3. Публикуете это объявление не чаще 1 раза в 30 дней.\n\n' \
           'Нажмите кнопку Платное объявление, если вы продаёте мёд ' \
           'или делаете ногти или предоставляете какие-либо услуги и пр. - это реклама (реклама платная).\n\n' \
           'За нарушение правил - блокировка.\n\n' \
           'При возникновении вопросов пишите боту @upskolkovohelpbot'

    return text


def advert_inf_text():
    text = "Вы выбрали платное размещение. " \
           "Перешлите сообщение выше ☝️ администратору: @UpSkolkovoHelpBot."

    return text

def success_send_text():
    text = 'Ваш запрос отправлен на модерацию!\n\n' \
           'При возникновении вопросов пишите @UpSkolkovoHelpBot'
    return text


def success_admin_accept_text(msg_id):
    text = 'Ваш запрос опубликован!'
    link = f'https://t.me/c/2129475388/{msg_id}'
    return f'{text}\n\n{link}'


""" Регистрация пользователя"""

def admin_confirm_photo_text(address, user_id):
    text=f'Новый пользователь {user_id} прислал фотографию дома\n' \
         f'Указанный адрес: {address}'
    return text