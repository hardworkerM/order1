from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db.storage import DatabaseManager

from data import config

# for local using
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# for server
# bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML, proxy=config.PROXY_URL)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = DatabaseManager('data/databases.db')
channel_id = config.CHANNEL_ID
admin_chat_id = config.ADMIN_CHANNEL_ID

