from aiogram.dispatcher.filters.state import State, StatesGroup


class topic_choice(StatesGroup):
    lvl1 = State()
    lvl2 = State()
    media_choice = State()
    text_handle = State()
    confirm = State()


class topic_choice_admin(StatesGroup):
    lvl1 = State()
    lvl2 = State()