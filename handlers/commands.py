from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import kb
import text
from states import CreateJew

commands_router = Router()


@commands_router.message(Command("start"))  # запускает обработчик только если входящее сообщение — команда /start
@commands_router.message(F.text == "⬅Назад(Выбор услуги)")
@commands_router.message(F.text == "Вернутся в главное меню")
async def start_handler(msg: Message, state: FSMContext):
    """Начально сообщение с выбором услуги"""
    await state.set_state(CreateJew.new_branch)
    if msg.text == "/start":
        user_msg = await msg.answer(text.welcome.format(name=msg.from_user.full_name), reply_markup=kb.menu)
        await state.update_data(user_msg=user_msg)
    else:
        await msg.answer(text.welcome_present_menu, reply_markup=kb.menu)
