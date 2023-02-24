
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

#from db import check_user_ad, add_ad
import message_texts


class StateAD(StatesGroup):
    text = State()
    button_title = State()
    button_url = State()
    view_limit = State()
    #completion = State()


async def _button_cancel():
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(
            text="Отменить создание",
            callback_data="cancel_ad"
        )
    )


async def create_ad__start(update: CallbackQuery, state: FSMContext):
    #check_ad = await check_user_ad(user_telegram_id=update.from_user.id)
    check_ad = True
    if check_ad is True:
        await StateAD.text.set()
        cache_message = await update.message.answer(
            text=message_texts.CREATE_AD__TEXT,
            reply_markup= await _button_cancel()
        )
        await state.update_data(cache_message=cache_message)
    else:
        await update.answer(
            text=message_texts.CREATE_AD__THERE_IS_AD,
            show_alert=True
        )

    await update.answer()


async def create_ad__text(update: Message, state: FSMContext):
    if len(update.text) < 200:
        await state.update_data(text=update.text)
        await StateAD.button_title.set()
        
        state_data = await state.get_data()
        cache_message: Message = state_data["cache_message"]
        await cache_message.delete()

        cache_message = await update.answer(
            text=message_texts.CREATE_AD__BUTTON_TITLE,
            reply_markup= await _button_cancel()
        )
        await state.update_data(cache_message=cache_message)

    else:
        await update.answer(text=message_texts.CREATE_AD__TEXT__INCORRECT)


async def create_ad__button_title(update: Message, state: FSMContext):
    if len(update.text) < 25:
        await state.update_data(button_title=update.text)
        await StateAD.button_url.set()
        
        state_data = await state.get_data()
        cache_message: Message = state_data["cache_message"]
        await cache_message.delete()

        cache_message = await update.answer(
            text=message_texts.CREATE_AD__BUTTON_URL,
            reply_markup= await _button_cancel()
        )
        await state.update_data(cache_message=cache_message)

    else:
        await update.answer(text=message_texts.CREATE_AD__BUTTON_TITLE__INCORRECT)


async def create_ad__button_url(update: Message, state: FSMContext):
    if update.text[:8] == "https://":
        await state.update_data(button_url=update.text)
        await StateAD.view_limit.set()
        
        state_data = await state.get_data()
        cache_message: Message = state_data["cache_message"]
        await cache_message.delete()

        cache_message = await update.answer(
            text=message_texts.CREATE_AD__VIEW_LIMIT,
            reply_markup= await _button_cancel()
        )
        await state.update_data(cache_message=cache_message)

    else:
        await update.answer(text=message_texts.CREATE_AD__BUTTON_URL__INCORRECT)


async def create_ad__view_limit(update: Message, state: FSMContext):
    try:
        required_value = int(update.text)
    except ValueError:
        await update.answer(text=message_texts.CREATE_AD__VIEW_LIMIT__INCORRECT)
    else:
        await state.update_data(view_limit=update.text)
        state_data = await state.get_data()
        await state.finish()

        """
        await add_ad(
            user_telegram_id=update.from_user.id,
            text=state_data["text"],
            button_title=state_data["button_title"],
            button_url=state_data["button_url"],
            view_limit=state_data["view_limit"]
        )
        """

        cache_message: Message = state_data["cache_message"]
        await cache_message.delete()
        await update.answer(text=message_texts.CREATE_AD__FINISH)


async def cancel_ad(update: CallbackQuery, state: FSMContext):
    await update.message.delete()
    await state.finish()
    await update.message.answer(text=message_texts.CREATE_AD__CANCEL)
    await update.answer()
