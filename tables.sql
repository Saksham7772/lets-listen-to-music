
CREATE TABLE performer (
    performer_id integer not null,
    name text not null
)

CREATE TABLE album (
    album_id integer not null,
    title text not null,
    performer integer not null,

    FOREIGN KEY (performer) REFERENCES performer (performer_id)
)

CREATE TABLE track (
    track_id integer not null,
    telegram_file_id text not null,
    title text not null,
    album integer not null,

    FOREIGN KEY (album) REFERENCES album (album_id)
)

CREATE TABLE dependence__track__performer (
    track_id integer not null,
    performer_id integer not null,

    FOREIGN KEY (track_id) REFERENCES track (track_id),
    FOREIGN KEY (performer_id) REFERENCES performer (performer_id)
)

;