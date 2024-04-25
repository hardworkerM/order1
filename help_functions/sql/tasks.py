from loader import db
from collections import defaultdict
import datetime, time
"""Не согласованы названия таблиц и колонок с функциями!"""


def filter_tasks(information):
    memo_to_update = []
    user_task = defaultdict(list)
    for task in information:
        user_id, title, description, memo_id = task
        txt = f'<b>{title}</b>\n\n{description}'
        user_task[user_id].append(txt)
        memo_to_update.append(memo_id)
    task_done(memo_to_update)
    return user_task


async def create_task_insert(id, title, msg, data):
    info = (id, title, msg, data, 0)
    db.query(f"INSERT INTO memo (user_id, title, description, date, status) VALUES {info}")


def take_date(date):
    information = db.fetchall(f"""SELECT user_id, title, description, memo_id 
                            FROM memo 
                            WHERE date = '{date}'
                            AND status = 0""")
    if not information:
        return 0
    user_task = filter_tasks(information)
    return user_task


def task_done(update):
    for m_id in update:
        db.query(f"""UPDATE memo 
                    SET status = 1
                    WHERE memo_id = {m_id}""")

"""МОИ"""

# упорядочивание по дате исполнения)))
def task_date_filter(task):
    y, m, d = [int(i) for i in task[2].split("-")]
    date_list = datetime.datetime(y, m, d)
    date_int = time.mktime(date_list.timetuple())
    return date_int


def task_list_in_text(tasks):
    text = '<b>Мои заметки:</b>\n\n'
    if not tasks:
        text += "У вас ещё нет заметок."
        return text
    tasks = sorted(tasks, key=task_date_filter)
    for i in tasks:
        title, description, task_date = i
        text += f'<b>{title}</b>\n{description}\nКогда:\n{task_date}\n\n'
    return text



def take_user_tasks(user_id):
    tasks = db.fetchall(f"""SELECT title, description, date
                            FROM memo
                            WHERE user_id = {user_id}""")
    return task_list_in_text(tasks)
