from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .mediagroup import AlbumMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(AlbumMiddleware())

    dp.middleware.setup(ThrottlingMiddleware(limit=.5))
