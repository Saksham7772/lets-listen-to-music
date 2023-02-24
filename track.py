
import os

from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from private_code.music import get_track_and_download
from db import get_track as get_track_db, add_track as add_track_db
from data_classes import Track


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
