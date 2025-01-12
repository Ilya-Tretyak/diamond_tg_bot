"""Create jew handlers, содержит код бота связанный с созданием заказа нового украшения.
 Будет состоять из функций-обработчиков с декораторами (фильтрами)"""

from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import kb
import text
from states import CreateJew

"""СОЗДАНИЕ ЮВЕЛИРНОГО УРКАШЕНИЕ НА ЗАКАЗ"""

create_jew_router = Router()


@create_jew_router.message(F.text == "Создание ювелирного изделия на заказ 💍")
@create_jew_router.message(CreateJew.jew_category)
async def create_jew_handler(msg: Message, state: FSMContext):
    """Выбор категории изделия"""
    await state.set_state(CreateJew.create_jew)
    await msg.answer(text.menu_jew_create, reply_markup=kb.menu_jew_create)


@create_jew_router.message(CreateJew.create_jew)
async def create_jew(msg: Message, state: FSMContext):
    """Выбор размера украшения."""
    await state.clear()
    await state.update_data(category=msg.text)
    if msg.text == "Кольцо":
        await state.set_state(CreateJew.jew_size)
        markup = kb.create_size_ring
    elif msg.text == "Цепь" or msg.text == "Браслет":
        await state.set_state(CreateJew.jew_size_chain)
        if msg.text == "Браслет":
            markup = kb.create_size_bracelet
        else:
            markup = kb.create_size_chain
    elif msg.text in ["Серьги", "Подвеска", "Пусеты", "Колье"]:
        await state.set_state(CreateJew.jew_size)
        await material_selection(msg, state)

    else:
        await state.set_state(CreateJew.about_jew)
        await about_jew(msg, state)
    await msg.answer(text.create_jew, reply_markup=markup)


@create_jew_router.message(F.text == "Другой размер")
async def different_gem(msg: Message, state: FSMContext):
    await msg.answer(text.different_size)


@create_jew_router.message(CreateJew.jew_size_chain)
async def weaving_selection(msg: Message, state: FSMContext):
    """Выбор плетения изделия"""
    if msg.text == "<Назад":
        await state.set_state(CreateJew.jew_category)
        await create_jew_handler(msg, state)
    else:
        await state.update_data(size=msg.text)
        await state.update_data(material="None")
        await state.set_state(CreateJew.jew_size)
        await msg.answer(text.weaving_chain, reply_markup=kb.weaving_chain)


@create_jew_router.message(CreateJew.jew_size)
async def material_selection(msg: Message, state: FSMContext):
    """Выбор материала для украшения."""
    data = await state.get_data()
    if msg.text == "<Назад":
        await state.set_state(CreateJew.jew_category)
        await create_jew_handler(msg, state)
    else:
        if "size" in data and data['material'] != "":
            await state.update_data(weaving=msg.text)
        elif msg.text in ["Серьги", "Подвеска", "Пусеты", "Колье"]:
            await state.update_data(size="Отсутствует")
            await state.update_data(weaving="Отсутствует")
        else:
            await state.update_data(size=msg.text)
            await state.update_data(weaving="Отсутствует")
        await state.set_state(CreateJew.jew_gem)
        await msg.answer(text.material_selection, reply_markup=kb.material_selection)


@create_jew_router.message(CreateJew.jew_gem)
async def gem(msg: Message, state: FSMContext):
    """Выбор наличия камней."""
    if msg.text == "<-Назад":
        await state.set_state(CreateJew.jew_category)
        await create_jew_handler(msg, state)
    else:
        await state.update_data(material=msg.text)
        await state.set_state(CreateJew.jew_gem_selection)
        await msg.answer(text.answer_have_gem, reply_markup=kb.have_gem)


@create_jew_router.message(CreateJew.jew_gem_selection)
async def gem_selection(msg: Message, state: FSMContext):
    """Выбор камня(Драгоценный/Полудрагоценный)"""
    if msg.text == "<--Назад":
        await state.set_state(CreateJew.jew_size)
        await state.update_data(material="")
        await material_selection(msg, state)
    elif msg.text == "Да ✅":
        await state.update_data(category_gem=msg.text)
        await state.set_state(CreateJew.about_jew)
        await msg.answer_photo(
            photo=types.FSInputFile(path="picturies/precious.jpeg"),
            caption="Выберите камень из предложенных или выберите 'Другой'",
            reply_markup=kb.gem_precious
        )
    else:
        await state.set_state(CreateJew.about_jew)
        await about_jew(msg, state)


@create_jew_router.message(CreateJew.about_jew and F.text == "Другой")
async def different_gem(msg: Message, state: FSMContext):
    await msg.answer(text.different_gem)


@create_jew_router.message(CreateJew.about_jew)
async def about_jew(msg: Message, state: FSMContext):
    """Об украшении(создание изделия по картинке, из каталога на сайте, другое)"""
    if msg.text == "<- Назад":
        await state.set_state(CreateJew.jew_gem)
        await gem(msg, state)
    else:
        if msg.text != "Брошь":
            await state.update_data(gem=msg.text)
        else:
            await state.update_data(size="Отсутствует")
            await state.update_data(weaving="Отсутствует")
            await state.update_data(material="Отсутствует")
            await state.update_data(gem="Отсутствует")
        await state.set_state(CreateJew.jew_view)
        await msg.answer(text.answer_about_jew, reply_markup=kb.about_jew)


@create_jew_router.message(F.text == "У меня есть фотография (похожего) украшения 🖼")
@create_jew_router.message(F.text == "Украшение из каталога 📔")
@create_jew_router.message(F.text == "Я еще не знаю что хочу...")
@create_jew_router.message(CreateJew.jew_view)
async def picture(msg: Message, state: FSMContext):
    """Отправка фотографии украшения от пользователя"""
    if msg.text == "<-- Назад":
        await state.set_state(CreateJew.jew_gem)
        await gem(msg, state)
    elif msg.text == "У меня есть фотография (похожего) украшения 🖼":
        await state.set_state(CreateJew.send_picture)
        await msg.answer(text.picture)
    elif msg.text == "Украшение из каталога 📔":
        await state.set_state(CreateJew.send_article)
        await msg.answer(text.article)
    elif msg.text == "Я еще не знаю что хочу...":
        await state.update_data(dont_know=msg.text)
        await state.set_state(CreateJew.send_dont_know)
        await msg.answer(text.send_dont_know, reply_markup=kb.send_dont_know)


@create_jew_router.message(CreateJew.send_picture)
async def send_picture(msg: Message, state: FSMContext):
    """Добавление фотографии"""
    await state.update_data(picture=msg.photo[-1].file_id)
    await state.set_state(CreateJew.view_order)
    await view_order(msg, state)


@create_jew_router.message(CreateJew.send_article)
async def send_article(msg: Message, state: FSMContext):
    """Добавление артикула с сайта"""
    await state.update_data(article=msg.text)
    await state.set_state(CreateJew.view_order)
    await view_order(msg, state)


@create_jew_router.message(CreateJew.view_order)
@create_jew_router.message(CreateJew.send_dont_know)
async def view_order(msg: Message, state: FSMContext):
    """Вывод итогового заказа для пользователя"""
    await msg.delete()
    await state.set_state(CreateJew.user_contact_share)
    data = await state.get_data()
    await msg.answer(
        f"<b>Уточним ваш заказ:</b>"
        f"\n\t•<i>Вид украшения:</i> \n    <b><i>{data['category']}</i></b>"
        f"\n\t•<i>Размер:</i> \n\t    <b><i>{data['size']}</i></b>"
        f"\n\t•<i>Плетение:</i> \n\t    <b><i>{data['weaving']}</i></b>"
        f"\n\t•<i>Материал:</i> \n\t    <b><i>{data['material']}</i></b>"
        f"\n\t•<i>Камень:</i> \n\t    <b><i>{data['gem']}</i></b>"
        f"\n\t<i>Изображение или артикул похожего украшения:</i>"
    )
    if 'picture' in data:
        await msg.answer_photo(data['picture'])
    elif 'article' in data:
        await msg.answer(f"<code>{data['article']}</code>")
    else:
        await msg.answer(data['dont_know'])
    await msg.answer(text.yes_or_no, reply_markup=kb.yes_or_no)


@create_jew_router.message(F.text == "Нет❌, заполнить анкету заново.")
async def unsuccessful_order(msg: Message, state: FSMContext):
    """Перенаправление на начало анкеты"""
    await state.set_state(CreateJew.create_jew)
    await msg.answer("Упс!🫣 Давайте попробуем еще раз", reply_markup=kb.menu_jew_create)


@create_jew_router.message(CreateJew.user_contact_share)
async def get_contact_user(msg: Message, state: FSMContext):
    """Получение контактного номера от пользователя"""
    await state.set_state(CreateJew.user_contact)
    await msg.answer(text.contact_user_share, reply_markup=kb.contact_keyboard)


@create_jew_router.message(CreateJew.user_contact)
async def successful_order(msg: Message, state: FSMContext):
    """Отправка информации по заказу и контактных данных менеджеру"""
    await state.update_data(user_contact=msg.contact.phone_number)
    data = await state.get_data()
    await state.bot.send_message(
        chat_id=314716345,
        text=\
        f"Заказ от {msg.from_user.full_name} \n username: {msg.from_user.username}"
        f"\nКонтактный номер: {data['user_contact']}"
        f"\n\t•<i>Вид украшения:</i> \n    <b><i>{data['category']}</i></b>"
        f"\n\t•<i>Размер:</i> \n\t    <b><i>{data['size']}</i></b>"
        f"\n\t•<i>Плетение:</i> \n\t    <b><i>{data['weaving']}</i></b>"
        f"\n\t•<i>Материал:</i> \n\t    <b><i>{data['material']}</i></b>"
        f"\n\t•<i>Камень:</i> \n\t    <b><i>{data['gem']}</i></b>"
        f"\n\t<i>Изображение или артикул похожего украшения:</i>"

    )
    if 'picture' in data:
        await state.bot.send_photo(chat_id=314716345, photo=data['picture'])
    elif 'article' in data:
        await state.bot.send_message(chat_id=314716345, text=f"<code>{data['article']}</code>")
    else:
        await state.bot.send_message(chat_id=314716345, text=data['dont_know'])
    await state.clear()
    await msg.answer(
        "\tОтлично, ваш заказ был создан и перенаправлен нашим мастерам."
        "\n\tВ ближайшее время мы с вами свяжемся и ответим на все необходимые вопросы."
        f"\n\t {msg.from_user.first_name}, мы рады что вы с нами♥"
        "\nС любовью, \n<i>'Ювелирный Дом Даймонд'</i>",
        reply_markup=kb.write_order_back
    )
