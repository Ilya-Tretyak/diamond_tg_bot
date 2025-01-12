""" Вспомогательные классы для FSM (машины состояний),
 а также фабрики Callback Data для кнопок Inline клавиатур"""


from aiogram.fsm.state import State, StatesGroup


class CreateJew(StatesGroup):
    new_branch = State()
    jew_category = State()
    create_jew = State()
    jew_size = State()
    jew_size_chain = State()
    jew_material = State()
    jew_gem = State()
    jew_gem_selection = State()
    about_jew = State()
    jew_view = State()
    jew_view_picture = State()
    send_picture = State()
    send_article = State()
    send_dont_know = State()
    view_order = State()
    user_contact = State()
    user_contact_share = State()


class RepairJew(StatesGroup):
    atelier_choice_job = State()
    atelier_choice_repair = State()
    atelier_choice_clean = State()
    atelier_choice_fix_stone = State()
    atelier_choice_remelting = State()
    atelier_jew_category = State()
    atelier_view_order = State()
    atelier_materials = State()
    atelier_send_picture = State()
    atelier_user_contact_share = State()
    atelier_user_contact = State()



