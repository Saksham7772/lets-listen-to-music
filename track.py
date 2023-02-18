
import os

from aiogram.types import Message

from private_code.music import track_download


async def track(update: Message):
    track_id = int(update.text[7:])

    # Getting a track from the database
    track = None

    if track is None:
        pathfile, track = await track_download(track_id=track_id)
        print(True)
