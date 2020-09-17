"""Configure bot, dispatcher, logger and polling"""
import os
import logging
from aiogram import Bot, Dispatcher, executor

# configure logger
logging.basicConfig(level=30, filename='main.log',
                    format='%(asctime)s <%(levelname)s> %(msg)s', datefmt='[%d-%m-%Y @ %H:%M:%S]')

# init bot and dispatcher
TOKEN = os.getenv('LANGUAGE_BOT_TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot)


def start(*tasks):
    """Start long-polling and tasks performing"""
    for task in tasks:
        dp.loop.create_task(task)
    executor.start_polling(dp, skip_updates=True)
