
from dataclasses import dataclass


@dataclass
class Performer:
    performer_id: int
    name: str


@dataclass
class Album:
    album_id: int
    title: str
    track_count: int
    performers: list[Performer]


@dataclass
class Track:
    track_id: int
    title: str
    album: Album
    performers: list[Performer]
    #file_tg: str
