from aiogram.dispatcher.filters.state import State, StatesGroup


class new_user(StatesGroup):
    home = State()
    got_photo = State()
    confirm = State()


# class answer_st(StatesGroup):