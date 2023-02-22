
import aiosqlite

import config
from data_classes import Track


async def get_track(track_id: int):
    async with aiosqlite.connect(config.SQLITE_PATH_DB) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "select"
            " t.track_id as track_id"
            ", t.title as track_title"
            " from track as t"
            f" where t.track_id={track_id}"
        ) as cursor:
            row = await cursor.fetchone()
            if row is not None:
                return Track(
                    track_id=row["track_id"],
                    title=row["track_title"],
                    album=None,
                    performers=None
                )
            else:
                return None


async def add_track():
    async with aiosqlite.connect(config.SQLITE_PATH_DB) as db:
        await db.execute(
            ""
        )
        await db.commit()
