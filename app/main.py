from aiogram import Bot, Dispatcher
from aiogram import executor

from app.handlers.client import register_client_handlers
from app.settings import TELEBOT_API_TOKEN

bot = Bot(token=TELEBOT_API_TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    register_client_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
