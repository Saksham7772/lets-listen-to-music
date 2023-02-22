
CREATE TABLE performer (
    performer_id integer not null,
    name text not null
);

CREATE TABLE album (
    album_id integer not null,
    title text not null,
    track_count integer not null
);

CREATE TABLE track (
    track_id integer not null,
    title text not null,
    album integer not null,

    FOREIGN KEY (album) REFERENCES album (album_id)
);

CREATE TABLE albums_of_performers (
    performer_id integer not null,
    album_id integer not null ,

    FOREIGN KEY (performer_id) REFERENCES performer (performer_id),
    FOREIGN KEY (album_id) REFERENCES album (album_id)
);

CREATE TABLE tracks_of_performers (
    performer_id integer not null,
    track_id integer not null,

    FOREIGN KEY (performer_id) REFERENCES performer (performer_id),
    FOREIGN KEY (track_id) REFERENCES track (track_id)
);

CREATE TABLE tracks_in_tg (
    track_id integer not null,
    file_tg text not null,

    FOREIGN KEY (track_id) REFERENCES track (track_id)
);
