
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardMarkup, InlineKeyboardButton
)

import message_texts


async def menu_ads(update: Message):
    await update.answer(
        text=message_texts.MENU_ADS,
        reply_markup=InlineKeyboardMarkup(row_width=1).add(
            InlineKeyboardButton(
                text="Создать рекламную интеграцию",
                callback_data="ads__create_ad"
            ),
            InlineKeyboardButton(
                text="Архив",
                callback_data="ads__archive"
            )
        )
    )
