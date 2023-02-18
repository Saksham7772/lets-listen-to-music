
import os

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage


""" Initialization Telegram Client """

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")

bot = Bot(token=TG_BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)
