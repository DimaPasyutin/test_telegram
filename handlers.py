from main import bot, dispatcher

from aiogram.types import Message
from config import admin_id


async def send_to_admin(dispatcher):
    await bot.send_message(admin_id, "Бот запущен")


@dispatcher.message_handler()
async def answer(message: Message):
    answer = "Чикибамбони, братишка"
    await message.answer(text=answer)
