from loader import db
from datetime import datetime
from aiogram import types


# вспомогаельная для парсинга
def parse_message(message: types.Message, state="None"):
    content_type = message.content_type
    chat_id = str(message.chat.id)
    username = message.from_user.username
    log_time = str(datetime.now())
    date = log_time[:10]+'T'+log_time[11:19]
    command_flg = "False"

    if content_type == 'text':
        text = message.text
        if text[0] == '/':
            if text in ['/start', '/help', '/change']:
                command_flg = "True"
    else:
        text = message.caption
    text = 'Пока нет'
    info = [chat_id, username, content_type, text, command_flg, state, date]
    print("################PARSED DATA:")
    print(info)
    return info


# внесение в бд
def insert_user_log(info):
    db.save_many(f"""INSERT INTO user_all_text VALUES (?, ?, ?, ?, ?, ?, ?)""", info)


def get_text():
    print('I am into get_text')
    res=db.fetchall('SELECT * FROM user_all_text')
    for i in res:
        print(i)