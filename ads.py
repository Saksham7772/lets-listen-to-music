
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
)
from aiogram.types.web_app_info import WebAppInfo

import message_texts


async def menu_ads(update: Message):
    await update.answer(
        text=message_texts.MENU_ADS,
        reply_markup=ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        ).add(
            KeyboardButton(
                text="Создать рекламную интеграцию",
                web_app=WebAppInfo(
                    url="https://spuxel.github.io/telegram-web-app-music/"
                )
            ) 
        )
    )


async def web_app(update: Message):
    await update.answer(text=update.web_app_data.data)
