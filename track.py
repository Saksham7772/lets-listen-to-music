
import os

from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from private_code.music import get_track_and_download, tracks_similar as music__tracks_similar
from db import get_track as get_track_db, add_track as add_track_db
from data_classes import Track
from pars import tracks_pars
import message_texts


async def track(update: Message):
    track_id = int(update.text[7:])
    track: Track = await get_track_db(track_id=track_id)

    _buttons = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(
            text="Похожие песни",
            callback_data=f"track__similar_{track_id}"
        )
    )

    if track is not None:
        await update.answer_audio(
            audio=track.file_tg,
            reply_markup=_buttons
        )

    else:
        track, pathfile = await get_track_and_download(track_id=track_id)
        sent_message = await update.answer_audio(
            audio=open(pathfile, "rb"),
            title=track.title,
            performer=", ".join([performer.name for performer in track.performers]),
            reply_markup=_buttons
        )

        await add_track_db(
            track=track,
            file_tg=sent_message.audio.file_id
        )

        if os.path.isfile(pathfile):
            os.remove(pathfile)


async def tracks_similar(update: CallbackQuery):
    similar = await music__tracks_similar(
        track_id=int(update.data[15:])
    )
    tracks = await tracks_pars(tracks=similar)
    if tracks is not None:
        await update.message.answer(text=tracks)
    else:
        await update.message.answer(text=message_texts.SEARCH_NO_RESULTS)
    await update.answer()
