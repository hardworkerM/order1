import schedule
import aioschedule
import asyncio

from help_functions.sql import analytics as analys
from help_functions.file_work import write

from loader import bot
import os
# Проверяется 1


async def send_db_to_admin():
    print('I AM IN send_db_to_admin')
    d = os.getcwd()
    path = d + '\\data\\databases.db'
    file = open(path, 'rb')
    await bot.send_document(565843474, file)
    file.close()


async def load_db_info():
    # достать все данные из файла
    info = write.read_out()

    # записать в бд
    analys.insert_user_log(info)

    # стереть все из файла
    write.empty_file()
    await bot.send_message(565843474, 'Database was uploaded')


# Каждый день происходит проверка
async def start_schedule():
    print("I am in start_schedule")
    aioschedule.every().day.at("00:01").do(load_db_info)
    aioschedule.every().day.at("00:02").do(send_db_to_admin)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
