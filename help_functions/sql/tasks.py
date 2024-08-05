from loader import db
from collections import defaultdict
import datetime, time
"""Не согласованы названия таблиц и колонок с функциями!"""
#
# self.query('CREATE TABLE IF NOT EXISTS '
#            'request (order_id int, user_id int, photos text, caption int)')


def convert_little(d):
    if len(d) == 1:
        return '0'+d
    return d


def make_order_id():
    date_now = datetime.datetime.now()
    y = convert_little(str(date_now.year)[-2:])
    m = convert_little(str(date_now.month))
    d =convert_little(str(date_now.day))
    h = convert_little(str(date_now.hour))
    min = convert_little(str(date_now.minute))
    s = convert_little(str(date_now.second))

    order_id_str =y + m + d + h + min + s
    order_id = int(order_id_str)
    return order_id


def new_request(order_id, user_id, content, caption, topic_lvl1, topic_lvl2):
    info = (order_id, user_id, content, caption, topic_lvl1, topic_lvl2)

    db.query(f"INSERT INTO request (order_id, user_id, content, caption, topic_lvl1, topic_lvl2) values {info}")


def find_order_info(user_id, order_id):
    order_info = db.fetchall(f"""SELECT * from request 
                                where user_id == {user_id} and order_id = {order_id}""")
    return order_info[-1]


def find_user_info(user_id):
    user_info = db.fetchall(f"""SELECT alias, name from user 
                                where id == {user_id}""")
    return user_info[0]
