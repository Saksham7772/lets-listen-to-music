
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


markup_main_menu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(
        text="Поиск",
        callback_data="main_menu__search"
    )
)
