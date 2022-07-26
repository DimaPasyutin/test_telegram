import asyncio

from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="Markdown")
dispatcher = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import dispatcher, send_to_admin
    executor.start_polling(dispatcher, on_startup=send_to_admin)
