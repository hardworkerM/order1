from loader import channel_id
from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class ChannelFilter(BoundFilter):
    async def check(self, message: types.Message):
        chat_id = message.chat.id
        return chat_id == channel_id

