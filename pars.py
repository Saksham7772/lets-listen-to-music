
async def _get_artists(obj) -> str:
    return ", ".join([artist.name for artist in obj.artists])


async def tracks_pars(tracks: list) -> str:
    message = "<b>Найденные песни:</b>"
    for track in tracks:
        track_artists = await _get_artists(obj=track)
        text_download = f"Скачать /track_{track.id}"
        message += f"\n\n<b>{track.title}</b> - {track_artists}\n{text_download}"

    return message
