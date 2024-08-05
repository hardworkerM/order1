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


def media_choice_text(lvl1, lvl2, n=0):
    text = '<b>Выберите медиа файлы для отправки</b>'
    how_much = f'Медиа: {n}/5'
    t1 = f'Тип: {lvl1}'
    t2 = f'Категория: {lvl2}'
    end = '<i>Нажмите Далее для добавления текста</i>'
    return f'{text}\n{how_much}\n{t1}\n{t2}\n\n{end}'


def text_choice_text(lvl1, lvl2, n=0):
    text = '<b>Введите текст объявления</b>'
    how_much = f'Медиа: {n}/5'
    t1 = f'Тип: {lvl1}'
    t2 = f'Категория: {lvl2}'
    return f'{text}\n{how_much}\n{t1}\n{t2}'


def add_meta_data_to_text(text, topic_lvl1, topic_lvl2, id, name, first_name):
    category = f'<b>Категории:</b> #{("").join(topic_lvl1.title().split())} ' \
               f'#{("").join(topic_lvl2.title().split())}'
    if name != 'None':
        connect = f'<b>Связатья:</b> @{name}(#ID{id})\ntg://user?id={id}'
    else:
        connect = f'<b>Связатья:</b>: В комментариях(#ID{id})\ntg://user?id={id}'
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
           "Ссылка на наш прайс лист: " \
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


def admin_confirm_photo_text(address, user_id, alias):
    head = '<b>Заявка на доступ к публикациям объявления</b>\n\n'

    if alias:
        user_info = f'<b>Username:</b> @{alias}\n'
    else:
        user_info = '<b>Username:</b> Отсутствует\n'
    house = f'<b>ID:</b> {user_id}\n' \
         f'<b>Номер дома:</b> {address}'
    return head+user_info + house


def admin_confirm_user_result(result, user_id, alias, address):
    publish_text = {'accept': '<b>Пользователь был принят\n\n</b>', 'deny': '<b>Заявка была отклонена\n\n</b>'}
    user_info = f'<b>ID:</b> {user_id}'
    user_info = f'<b>Username:</b> {alias}\n' + user_info +'\n'
    house = f'<b>Номер дома:</b> {address}'
    return publish_text[result] + user_info + house


def confirm_user_success():
    text = 'Ваш профиль подтвержден!\n' \
           'Для начала работы с ботом нажмите на кнопку приступить'
    return text


def confirm_user_fail():
    text = 'К сожалению фотография и адрес не прошли модерацию'

    return text