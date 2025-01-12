"""Точка входа, код запуска бота и инициализации всех остальных модулей"""

import asyncio  # — для асинхронного запуска бота
import logging  # — для настройки логгирования, которое поможет в отладке

from aiogram import Bot, Dispatcher  # — основной модуль библиотеки aiogram, импортируем классы Bot и Dispatcher
from aiogram.enums.parse_mode import ParseMode  # — содержит настройки разметки сообщений (HTML, Markdown)
from aiogram.fsm.storage.memory import MemoryStorage  # — хранилища данных для состояний пользователей
import config  # настройки бота
from handlers.commands import commands_router
from handlers.create_jew_handlers import create_jew_router
from handlers.atelier_handlers import atelier_router


bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    dp.include_routers(
        commands_router,
        create_jew_router,
        atelier_router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
