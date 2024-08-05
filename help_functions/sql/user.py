from loader import db


# Проверяет есть ли данные о пользователе
def check_user(user_id):
    user = db.fetchall(f"""SELECT u.id FROM user u
                       WHERE u.id = {user_id}""")
    if user:
        return 1
    return 0

"""ВЕРИФИКАЦИЯ ПОЛЬЗОВАТЕЛЯ"""
def check_user_verified(user_id):
    flag = db.fetchall(f"""select verified from user where id = {user_id}""")
    print(user_id)
    print(flag)
    if flag:
        return flag[0][0]
    return 0


def update_user_verification(user_id):
    print(user_id)
    q = f'UPDATE user SET verified=1 WHERE id={user_id}'
    db.query(q)


# Вносит данные о новом пользователе
def main_info_fill(id, alias, name, verified=0):
    if not alias:
        alias = 'None'
    info = (id, alias, name, verified)
    db.query(f'INSERT INTO user (id, alias, name, verified)  VALUES {info}')