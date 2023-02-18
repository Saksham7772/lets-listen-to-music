
from aiogram.types import Message, CallbackQuery

import message_texts
from private_code.music import search_tracks as music__search_tracks
from pars import tracks_pars


async def search(update: CallbackQuery):
    await update.message.answer(text=message_texts.SEARCH)
    await update.answer()


async def search_tracks(update: Message):
    tracks = await music__search_tracks(search_request=update.text)

    if tracks is not None:
        message = await tracks_pars(tracks=tracks.tracks.results)
        await update.answer(text=message)

    else:
        await update.answer(text=message_texts.SEARCH_NO_RESULTS, reply=True)
