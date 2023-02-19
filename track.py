
import os

from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from private_code.music import track_download


async def track(update: Message):
    track_id = int(update.text[7:])

    # Getting a track from the database
    track = None

    if track is None:
        pathfile, track = await track_download(track_id=track_id)
        await update.answer_audio(
            audio=open(pathfile, "rb"),
            title=track.title,
            performer=", ".join([performer.name for performer in track.artists]),
            reply_markup=InlineKeyboardMarkup(row_width=1).add(
                InlineKeyboardButton(
                    text="Похожие песни",
                    callback_data=f"track__similar_{track_id}"
                )
            )
        )

        if os.path.isfile(pathfile):
            os.remove(pathfile)

        print(True)
