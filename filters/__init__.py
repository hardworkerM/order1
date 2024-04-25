from aiogram import Dispatcher

from loader import dp
from .is_correct_channel import ChannelFilter


if __name__ == "filters":
    dp.filters_factory.bind(ChannelFilter)
    pass
