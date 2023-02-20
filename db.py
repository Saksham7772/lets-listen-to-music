
from dataclasses import dataclass

import aiosqlite

import config


@dataclass
class Performer:
    performer_id: int
    name: str


@dataclass
class Album:
    album_id: int
    title: str
    performer: Performer


@dataclass
class Track:
    track_id: int
    track_tg_file_id: str
    title: str
    #album: Album
    #performers: list[Performer]


async def get_track(track_id: int):
    async with aiosqlite.connect(config.SQLITE_PATH_DB) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "select"
            " t.track_id as track_id"
            ", t.telegram_file_id as track_tg_file_id"
            ", t.title as track_title"
            " from track as t"
            f" where t.track_id={track_id}"
        ) as cursor:
            row = await cursor.fetchone()
            return Track(
                track_id=row["track_id"],
                track_tg_file_id=row["track_tg_file_id"],
                title=row["track_title"]
            )
