from aiogram import Dispatcher

from loader import dp
from .is_correct_channel import ChannelFilter, TimeFilter


if __name__ == "filters":
    dp.filters_factory.bind(ChannelFilter)
    dp.filters_factory.bind(TimeFilter)
    pass
