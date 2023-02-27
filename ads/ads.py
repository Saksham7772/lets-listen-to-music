
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.types.web_app_info import WebAppInfo

import message_texts


async def menu_ads(update: Message):
    await update.answer(
        text=message_texts.MENU_ADS,
        reply_markup=InlineKeyboardMarkup(row_width=1).add(
            InlineKeyboardButton(
                text="Создать рекламную интеграцию",
                #callback_data="ads__create_ad"
                web_app=WebAppInfo(url="https://www.google.ru")
            ),
            InlineKeyboardButton(
                text="Архив",
                callback_data="ads__archive"
            )
        )
    )
