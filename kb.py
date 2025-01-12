""" Все клавиатуры, используемые ботом."""

from aiogram.types import (
        KeyboardButton,
        ReplyKeyboardMarkup,
)



menu_button = [
        [KeyboardButton(text="Создание ювелирного изделия на заказ 💍", callback_data="create_jew")],
        [KeyboardButton(text="Услуги мастерской 💎", callback_data="jew_studio")]
]
"""Reply клавиатура, выбор услуги"""
menu = ReplyKeyboardMarkup(keyboard=menu_button, resize_keyboard=True)


menu_jew_create_button = [
        [KeyboardButton(text="⬅Назад(Выбор услуги)", callback_data="jew_style")],
        [KeyboardButton(text="Кольцо", callback_data="jew_style")],
        [KeyboardButton(text="Серьги", callback_data="jew_style")],
        [KeyboardButton(text="Браслет", callback_data="jew_style")],
        [KeyboardButton(text="Подвеска", callback_data="jew_style")],
        [KeyboardButton(text="Колье", callback_data="jew_style")],
        [KeyboardButton(text="Пусеты", callback_data="jew_style")],
        [KeyboardButton(text="Брошь", callback_data="jew_style")],
        [KeyboardButton(text="Цепь", callback_data="jew_style")],
]
"""Reply клавиатура, выбор категории изделия"""
menu_jew_create = ReplyKeyboardMarkup(keyboard=menu_jew_create_button)


create_size_ring_button = [
        [KeyboardButton(text="<Назад")],
        [KeyboardButton(text="15", callback_data="15"),
         KeyboardButton(text="15.5", callback_data="15.5"),
         KeyboardButton(text="16", callback_data="16")],
        [KeyboardButton(text="16.5", callback_data="16.5"),
         KeyboardButton(text="17", callback_data="17"),
         KeyboardButton(text="17.5", callback_data="17.5")],
        [KeyboardButton(text="18", callback_data="18"),
         KeyboardButton(text="18.5", callback_data="18.5"),
         KeyboardButton(text="19", callback_data="19")],
        [KeyboardButton(text="19.5", callback_data="19.5"),
         KeyboardButton(text="20", callback_data="20"),
         KeyboardButton(text="Другой размер", callback_data="size")],
]
"""ReplyKeyboard клавиатура, выбор размера кольца"""
create_size_ring = ReplyKeyboardMarkup(keyboard=create_size_ring_button)


create_size_chain_button = [
        [KeyboardButton(text="<Назад")],
        [KeyboardButton(text="40 см", callback_data="40"),
         KeyboardButton(text="45 см", callback_data="45"),
         KeyboardButton(text="50 см", callback_data="50")],
        [KeyboardButton(text="55 см", callback_data="55"),
         KeyboardButton(text="60 см", callback_data="60"),
         KeyboardButton(text="65 см", callback_data="65")],
        [KeyboardButton(text="70 см", callback_data="70"),
         KeyboardButton(text="75 см", callback_data="75"),
         KeyboardButton(text="80 см", callback_data="80")],
        [KeyboardButton(text="85 см", callback_data="85"),
         KeyboardButton(text="90 см", callback_data="90"),
         KeyboardButton(text="Другой размер", callback_data="size")],
]
"""ReplyKeyboard клавиатура, выбор размера цепи"""
create_size_chain = ReplyKeyboardMarkup(keyboard=create_size_chain_button)


create_size_bracelet_button = [
        [KeyboardButton(text="<Назад")],
        [KeyboardButton(text="16", callback_data="16"),
         KeyboardButton(text="16,5", callback_data="16,5"),
         KeyboardButton(text="17", callback_data="17")],
        [KeyboardButton(text="17,5", callback_data="17,5"),
         KeyboardButton(text="18", callback_data="18"),
         KeyboardButton(text="18,5", callback_data="18,5")],
        [KeyboardButton(text="19", callback_data="19,5"),
         KeyboardButton(text="20", callback_data="20"),
         KeyboardButton(text="20,5", callback_data="20,5")],
        [KeyboardButton(text="21", callback_data="21"),
         KeyboardButton(text="21,5", callback_data="21,5"),
         KeyboardButton(text="Другой размер", callback_data="size")],
]
create_size_bracelet = ReplyKeyboardMarkup(keyboard=create_size_bracelet_button)


weaving_chain_button = [
    [KeyboardButton(text="<-Назад")],
    [KeyboardButton(text="Якорное", callback_data="anchor"),
     KeyboardButton(text="Бисмарк", callback_data="bismark")],
    [KeyboardButton(text="Курад", callback_data="kurad"),
     KeyboardButton(text="Картье", callback_data="cartier")],
    [KeyboardButton(text="Панцирное", callback_data="shell"),
     KeyboardButton(text="Верёвочка", callback_data="rope")],
    [KeyboardButton(text="Фантазийное", callback_data="fantasy"),
     KeyboardButton(text="Кобра", callback_data="cobra")],
    [KeyboardButton(text="Королевская мантия", callback_data="royal_mantle"),
     KeyboardButton(text="Царское", callback_data="king")],
    [KeyboardButton(text="Итальянское", callback_data="italy"),
     KeyboardButton(text="Я не уверен(а), какую хочу", callback_data="not")]
]
"""ReplyKeyboard клавиатура, выбор плетения цепи"""
weaving_chain = ReplyKeyboardMarkup(keyboard=weaving_chain_button)


material_selection_button = [
        [KeyboardButton(text="<-Назад")],
        [KeyboardButton(text="Желтое золото", callback_data="yellow_gold")],
        [KeyboardButton(text="Белое золото", callback_data="white_gold")],
        [KeyboardButton(text="Красное золото", callback_data="red_gold")],
        [KeyboardButton(text="Серебро", callback_data="silver")],
]
"""Reply клавиатура, материал украшения"""
material_selection = ReplyKeyboardMarkup(keyboard=material_selection_button)


have_gem_button = [
        [KeyboardButton(text="<--Назад")],
        [KeyboardButton(text="Да ✅", callback_data="have_gem"),
         KeyboardButton(text="Нет ❌", callback_data="have_gem")],
]
have_gem = ReplyKeyboardMarkup(keyboard=have_gem_button, resize_keyboard=True)


gem_precious_button = [
        [KeyboardButton(text="<- Назад")],
        [KeyboardButton(text="Алмаз", callback_data="precious")],
        [KeyboardButton(text="Изумруд", callback_data="precious")],
        [KeyboardButton(text="Сапфир", callback_data="precious")],
        [KeyboardButton(text="Гранат", callback_data="precious")],
        [KeyboardButton(text="Рубин", callback_data="precious")],
        [KeyboardButton(text="Аквамарин", callback_data="precious")],
        [KeyboardButton(text="Желтый топаз", callback_data="precious")],
        [KeyboardButton(text="Другой", callback_data="precious")],
]
gem_precious = ReplyKeyboardMarkup(keyboard=gem_precious_button)


about_jew_button = [
        [KeyboardButton(text="<-- Назад")],
        [KeyboardButton(text="У меня есть фотография (похожего) украшения 🖼", callback_data="about_jew")],
        [KeyboardButton(text="Украшение из каталога 📔", callback_data="about_jew")],
        [KeyboardButton(text="Я еще не знаю что хочу...", callback_data="about_jew")],
]
"""Reply клавиатура, какое украшение хочет клиент"""
about_jew = ReplyKeyboardMarkup(keyboard=about_jew_button)


send_dont_know_button = [
    [KeyboardButton(text="Отлично🔥", callback_data="dont_know")],
]

send_dont_know = ReplyKeyboardMarkup(keyboard=send_dont_know_button, resize_keyboard=True)


yes_or_no_button = [
        [KeyboardButton(text="Да✅, все верно.")],
        [KeyboardButton(text="Нет❌, заполнить анкету заново.")],
]
yes_or_no = ReplyKeyboardMarkup(keyboard=yes_or_no_button, resize_keyboard=True)


write_order_back_button = [
        [KeyboardButton(text="Вернутся в главное меню")],
]
write_order_back = ReplyKeyboardMarkup(keyboard=write_order_back_button, resize_keyboard=True)


contact_keyboard_button = [
        [KeyboardButton(text="📱 Отправить", request_contact=True)],
]
contact_keyboard = ReplyKeyboardMarkup(keyboard=contact_keyboard_button, resize_keyboard=True)

"""УСЛУГИ МАСТЕРСКОЙ"""

atelier_choice_job_button = [
    [KeyboardButton(text="Ремонт изделия")],
    [KeyboardButton(text="Чистка изделия")],
    [KeyboardButton(text="Закрепка камней")],
    [KeyboardButton(text="Переплав изделия")],
]
atelier_choice_job = ReplyKeyboardMarkup(keyboard=atelier_choice_job_button, resize_keyboard=True)


atelier_choice_jew = ReplyKeyboardMarkup(
    keyboard=menu_jew_create_button,
    resize_keyboard=True
)


repair_choice_ring_button = [
    [KeyboardButton(text="Изменение размера кольца")],
    [KeyboardButton(text="Пайка разлома")],
    [KeyboardButton(text="Правка кольца")],
    [KeyboardButton(text="Я не уверен(а)")],
]
repair_choice_ring = ReplyKeyboardMarkup(keyboard=repair_choice_ring_button)


repair_choice_earrings_button = [
    [KeyboardButton(text="Ремонт иглы замка")],
    [KeyboardButton(text="Ремонт фиксации замка")],
    [KeyboardButton(text="Ремонт штифта замка")],
    [KeyboardButton(text="Ремонт механизма удержания серьги в ухе")],
    [KeyboardButton(text="Я не уверен(а)")],
]
repair_choice_earrings = ReplyKeyboardMarkup(keyboard=repair_choice_earrings_button)


repair_choice_poussettes_button = [
    [KeyboardButton(text="Замена пусеты")],
    [KeyboardButton(text="Ремонт резьбы пусеты")],
    [KeyboardButton(text="Я не уверен(а)")],
]
repair_choice_poussettes = ReplyKeyboardMarkup(keyboard=repair_choice_poussettes_button)


repair_choice_bracelet_button = [
    [KeyboardButton(text="Уменьшение браслета")],
    [KeyboardButton(text="Ремонт каучуковых браслетов ")],
    [KeyboardButton(text="Ремонт браслета с камнями ")],
    [KeyboardButton(text="Я не уверен(а)")],
]
repair_choice_bracelet = ReplyKeyboardMarkup(keyboard=repair_choice_bracelet_button)


repair_choice_chain_button = [
    [KeyboardButton(text="Ремонт цепочки")],
    [KeyboardButton(text="Ремонт пустотелой цепочки ")],
    [KeyboardButton(text="Ремонт порванных пополам цепочек ")],
    [KeyboardButton(text="Замена законцовки")],
    [KeyboardButton(text="Изменение размера цепочки")],
    [KeyboardButton(text="Восстановление растянутых звеньев")],
    [KeyboardButton(text="Я не уверен(а)")],
]
repair_choice_chain = ReplyKeyboardMarkup(keyboard=repair_choice_chain_button)


repair_ring_size_button = [
    [KeyboardButton(text="Увеличение размера")],
    [KeyboardButton(text="Уменьшение размера")],
]
repair_ring_size = ReplyKeyboardMarkup(keyboard=repair_ring_size_button, resize_keyboard=True)


ring_size_count_button = [
    [KeyboardButton(text="1")],
    [KeyboardButton(text="2")],
]
ring_size_count = ReplyKeyboardMarkup(keyboard=ring_size_count_button, resize_keyboard=True)


atelier_picture_button = [
    [KeyboardButton(text="Отсутствует")],
]
atelier_picture = ReplyKeyboardMarkup(keyboard=atelier_picture_button, resize_keyboard=True)


atelier_choice_clear_button = [
    [KeyboardButton(text="Отжиг ")],
    [KeyboardButton(text="Чистка ")],
    [KeyboardButton(text="Полировка ")],
    [KeyboardButton(text="Родирование ")],
    [KeyboardButton(text="Я не уверен(а)")]
]
atelier_choice_clear = ReplyKeyboardMarkup(keyboard=atelier_choice_clear_button)


atelier_choice_fix_stone_button = [
    [KeyboardButton(text="Закрепка камня")],
    [KeyboardButton(text=" Раскрепка камня")]
]
atelier_choice_fix_stone = ReplyKeyboardMarkup(keyboard=atelier_choice_fix_stone_button)


atelier_choice_remelting_button = [
    [KeyboardButton(text="Переплавка")],
    [KeyboardButton(text="Переплавка под изготовление нового изделия ")],
    [KeyboardButton(text="Я не уверен(а)")]
]
atelier_choice_remelting = ReplyKeyboardMarkup(keyboard=atelier_choice_remelting_button)

atelier_yes_or_no_button = [
        [KeyboardButton(text="Да✅, все верно.")],
        [KeyboardButton(text="Нет❌, заполнить заказ заново.")],
]
atelier_yes_or_no = ReplyKeyboardMarkup(keyboard=atelier_yes_or_no_button, resize_keyboard=True)
