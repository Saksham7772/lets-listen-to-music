
from aiogram.types import Message

import message_texts
from markups import markup_main_menu


async def main_menu(update: Message):
    await update.answer(text=message_texts.MAIN_MENU, reply_markup=markup_main_menu)
