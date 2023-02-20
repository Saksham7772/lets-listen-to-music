
from dataclasses import dataclass


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
