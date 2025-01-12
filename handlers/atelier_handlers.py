"""Atelier_handlers, содержит код бота связанный с созданием заказа ремонта украшения.
 Будет состоять из функций-обработчиков с декораторами (фильтрами)"""

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import kb
import text
from states import RepairJew

"""УСЛУГИ МАСТЕРСКОЙ"""

atelier_router = Router()


@atelier_router.message(F.text == "Услуги мастерской 💎")
async def atelier_choice_job(msg: Message, state: FSMContext):
    """Выбор вида работы мастерской"""
    await state.set_state(RepairJew.atelier_jew_category)
    await msg.answer(text.atelier_jew, reply_markup=kb.atelier_choice_job)


@atelier_router.message(RepairJew.atelier_jew_category)
@atelier_router.message(F.text == "<-Назад")
async def repair_choice_jew(msg: Message, state: FSMContext):
    """Выбор изделия для ремонта"""
    if msg.text != "<-Назад":
        await state.update_data(atelier_choice_job=msg.text)
    data = await state.get_data()
    if data["atelier_choice_job"] == "Ремонт изделия":
        await state.set_state(RepairJew.atelier_choice_repair)
    elif data["atelier_choice_job"] == "Чистка изделия":
        await state.set_state(RepairJew.atelier_choice_clean)
    elif data["atelier_choice_job"] == "Закрепка камней":
        await state.set_state(RepairJew.atelier_choice_fix_stone)
    elif data["atelier_choice_job"] == "Переплав изделия":
        await state.set_state(RepairJew.atelier_choice_remelting)
    await msg.answer(text.atelier_choice_jew, reply_markup=kb.menu_jew_create)


@atelier_router.message(RepairJew.atelier_choice_repair)
async def repair_choice_ring(msg: Message, state: FSMContext):
    """Выбор вида ремонта для изделий"""
    data = await state.get_data()
    await state.update_data(jew_selection=msg.text)
    await state.set_state(RepairJew.atelier_materials)
    if msg.text == "Кольцо":
        await msg.answer(text.repair_choice_jews, reply_markup=kb.repair_choice_ring)
    elif msg.text == "Серьги":
        await msg.answer(text.repair_choice_jews, reply_markup=kb.repair_choice_earrings)
    elif msg.text == "Пусеты":
        await msg.answer(text.repair_choice_jews, reply_markup=kb.repair_choice_poussettes)
    elif msg.text == "Цепь":
        await msg.answer(text.repair_choice_jews, reply_markup=kb.repair_choice_chain)
    elif msg.text == "Браслет":
        await msg.answer(text.repair_choice_jews, reply_markup=kb.repair_choice_bracelet)


@atelier_router.message(F.text == "Изменение размера кольца")
async def repair_ring_size(msg: Message, state: FSMContext):
    """Выбор увеличение/уменьшение кольца"""
    await state.update_data(repair_choice_job=msg.text)
    await msg.answer(text.ring_size, reply_markup=kb.repair_ring_size)


@atelier_router.message(F.text == "Увеличение размера")
@atelier_router.message(F.text == "Уменьшение размера")
async def repair_ring_size_count(msg: Message, state: FSMContext):
    """Выбор размера увеличение/уменьшение кольца"""
    await state.update_data(ring_size_more_less=msg.text)
    await state.set_state(RepairJew.atelier_materials)
    await msg.answer(text.ring_size_count, reply_markup=kb.ring_size_count)


@atelier_router.message(RepairJew.atelier_choice_clean)
async def atelier_choice_clear(msg: Message, state: FSMContext):
    """Выбор способа чистки"""
    await state.update_data(jew_selection=msg.text)
    await state.set_state(RepairJew.atelier_materials)
    await msg.answer(text.clear, reply_markup=kb.atelier_choice_clear)


@atelier_router.message(RepairJew.atelier_choice_fix_stone)
async def atelier_choice_fix_stone(msg: Message, state: FSMContext):
    """Закрепить/Открепить камень"""
    await state.update_data(jew_selection=msg.text)
    await state.set_state(RepairJew.atelier_materials)
    await msg.answer(text.fix_stone, reply_markup=kb.atelier_choice_fix_stone)


@atelier_router.message(RepairJew.atelier_choice_remelting)
async def atelier_choice_remelting(msg: Message, state: FSMContext):
    """Переплав изделия"""
    await state.update_data(jew_selection=msg.text)
    await state.set_state(RepairJew.atelier_materials)
    await msg.answer(text.fix_stone, reply_markup=kb.atelier_choice_remelting)


@atelier_router.message(RepairJew.atelier_materials)
async def repair_materials(msg: Message, state: FSMContext):
    """Выбор материала изделия"""
    data = await state.get_data()
    await state.set_state(RepairJew.atelier_send_picture)
    if msg.text in ["1", "2"]:
        await state.update_data(ring_size_count=msg.text)
    else:
        await state.update_data(repair_choice_job=msg.text)
    await msg.answer(text.materials, reply_markup=kb.material_selection)


@atelier_router.message(RepairJew.atelier_send_picture)
async def send_picture(msg: Message, state: FSMContext):
    """Отправка фотографии изделия от пользователя"""
    await state.update_data(material=msg.text)
    await state.set_state(RepairJew.atelier_view_order)
    await msg.answer(text.atelier_picture, reply_markup=kb.atelier_picture)


@atelier_router.message(RepairJew.atelier_view_order)
async def atelier_view_order(msg: Message, state: FSMContext):
    """Уточнение корректности заказа"""
    if msg.text != "Отсутствует":
        await state.update_data(repair_picture=msg.photo[-1].file_id)
    await state.set_state(RepairJew.atelier_user_contact_share)
    data = await state.get_data()
    await msg.answer("<b>Уточним ваш заказ:</b>")
    await msg.answer(
        f"\n\t<b><i>{data['atelier_choice_job']}</i></b>"
        f"\n\t•<i>Вид изделия:</i> \n\t    <b><i>{data['jew_selection']}</i></b>"
        f"\n\t•<i>Материал изделия:</i> \n\t    <b><i>{data['material']}</i></b>"
        f"\n\t<i>Вид ремонта:</i> "
        f"\n\t    <b><i>{data['repair_choice_job']}</i></b> "
    )
    if 'ring_size_more_less' in data:
        await msg.answer(
            f"\n\t    •<b><i>{data['ring_size_more_less']} на {data['ring_size_count']}</i></b>"
        )
    if 'repair_picture' in data and data['repair_picture'] != "Отсутствует":
        await msg.answer("\n\t<i>Изображение украшения:</i>")
        await msg.answer_photo(data['repair_picture'])
    else:
        await msg.answer("\n\t<i>Изображение украшения:</i>")
        await msg.answer("\n\t<i> -Отсутствует</i>")
    await msg.answer(text.yes_or_no, reply_markup=kb.atelier_yes_or_no)


@atelier_router.message(F.text == "Нет❌, заполнить заказ заново.")
async def unsuccessful_order(msg: Message, state: FSMContext):
    """Перенаправление на начало анкеты"""
    await state.set_state(RepairJew.atelier_jew_category)
    await msg.answer("Упс!🫣 Давайте попробуем еще раз", reply_markup=kb.atelier_choice_job)


@atelier_router.message(RepairJew.atelier_user_contact_share)
async def get_contact_user(msg: Message, state: FSMContext):
    """Получение контактного номера от пользователя"""
    await state.set_state(RepairJew.atelier_user_contact)
    await msg.answer(text.contact_user_share, reply_markup=kb.contact_keyboard)


@atelier_router.message(RepairJew.atelier_user_contact)
async def successful_order(msg: Message, state: FSMContext):
    """Отправка информации по заказу и контактных данных менеджеру"""
    await state.update_data(user_contact=msg.contact.phone_number)
    data = await state.get_data()
    await state.bot.send_message(
        chat_id=314716345,
        text=f"Заказ от {msg.from_user.full_name} \n username: @{msg.from_user.username}"
        f"\nКонтактный номер: {data['user_contact']}"
        f"\n\t<b><i>{data['atelier_choice_job']}</i></b>"
        f"\n\t•<i>Вид изделия:</i> \n\t    <b><i>{data['jew_selection']}</i></b>"
        f"\n\t•<i>Материал изделия:</i> \n\t    <b><i>{data['material']}</i></b>"
        f"\n\t<i>Вид ремонта:</i> "
        f"\n\t    <b><i>{data['repair_choice_job']}</i></b> "
    )
    if 'ring_size_more_less' in data:
        await state.bot.send_message(
            chat_id=314716345,
            text=f"\n\t    <b><i>{data['ring_size_more_less']} на {data['ring_size_count']}</i></b>"
        )
    if 'repair_picture' in data and data['repair_picture'] != "Отсутствует":
        await state.bot.send_message(chat_id=314716345, text="\n\t<i>Изображение украшения:</i>")
        await state.bot.send_photo(chat_id=314716345, photo=data['repair_picture'])
    else:
        await state.bot.send_message(chat_id=314716345, text="\n\t<i>Изображение украшения: Отсутствует</i>")
        await state.bot.send_message(chat_id=314716345, text="\n\t<i> -Отсутствует</i>")
    await state.clear()
    await msg.answer(
        "\tОтлично, ваш заказ был создан и перенаправлен нашим мастерам."
        "\n\tВ ближайшее время мы с вами свяжемся и ответим на все необходимые вопросы."
        f"\n\t {msg.from_user.first_name}, спасибо за доверие♥"
        "\nС любовью, \n<i>'Ювелирный Дом Даймонд'</i>",
        reply_markup=kb.write_order_back
    )
