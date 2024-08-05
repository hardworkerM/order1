from loader import channel_id
from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
import datetime


class ChannelFilter(BoundFilter):
    async def check(self, message: types.Message):
        chat_id = message.chat.id
        return chat_id == channel_id

class TimeFilter(BoundFilter):
    async def check_time(self):
        time_now = datetime.datetime.now()
        hour = time_now.hour
        return hour < 23