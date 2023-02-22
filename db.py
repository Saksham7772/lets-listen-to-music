
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


async def add_track(track: Track, file_tg: str):
    async with aiosqlite.connect(config.SQLITE_PATH_DB) as db:

        # Add data to the performer table
        for performer in track.performers:
            await db.execute(
                "insert into performer"
                " (performer_id, name)"
                " values (?,?)",
                (performer.performer_id, performer.name)
            )

        # Add data to the album table
        await db.execute(
            "insert into album"
            " (album_id, title, track_count)"
            " values (?,?,?)",
            (
                track.album.album_id,
                track.album.title,
                track.album.track_count
            )
        )

        # Add data to the track table
        await db.execute(
            "insert into track"
            " (track_id, title, album)"
            " values (?,?,?)",
            (track.track_id, track.title, track.album.album_id)
        )

        # Add data to the albums_of_performers table
        for performer in track.album.performers:
            await db.execute(
                "insert into albums_of_performers"
                " (performer_id, album_id)"
                " values (?,?)",
                (performer.performer_id, track.album.album_id)
            )

        # Add data to the tracks_of_performers table
        for performer in track.performers:
            await db.execute(
                "insert into tracks_of_performers"
                " (performer_id, track_id)"
                " values (?,?)",
                (performer.performer_id, track.track_id)
            )

        # Add data to the tracks_in_tg table
        await db.execute(
            "insert into tracks_in_tg"
            " (track_id, file_tg)"
            " values (?,?)",
            (track.track_id, file_tg)
        )

        await db.commit()
