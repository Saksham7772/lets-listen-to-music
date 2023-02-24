
from aiogram.dispatcher.filters.builtin import \
    CommandStart, CommandHelp, IDFilter, IsReplyFilter, \
    ChatTypeFilter, ChatType

from tg import dispatcher
from main_menu import main_menu
from search import search, search_tracks
from filters import SearchFilter
from track import track, tracks_similar
from ads.ads import menu_ads
from ads.create_ad import (
    StateAD, create_ad__start,
    create_ad__text,
    create_ad__button_title, create_ad__button_url,
    create_ad__view_limit,
    cancel_ad
)


# MAIN MENU
dispatcher.register_message_handler(
    main_menu, ChatTypeFilter(chat_type=ChatType.PRIVATE), CommandStart()
)
dispatcher.register_message_handler(
    main_menu, ChatTypeFilter(chat_type=ChatType.PRIVATE), text="/menu"
)
dispatcher.register_message_handler(
    main_menu, ChatTypeFilter(chat_type=ChatType.PRIVATE), text="//"
)


# SEARCH
dispatcher.register_callback_query_handler(
    search, text="main_menu__search"
)
dispatcher.register_message_handler(
    search_tracks,
    ChatTypeFilter(chat_type=ChatType.PRIVATE),
    IsReplyFilter(is_reply=True),
    SearchFilter()
)

# TRACK
dispatcher.register_message_handler(
    track, ChatTypeFilter(chat_type=ChatType.PRIVATE), text_startswith="/track_"
)

# TRACKS SIMILAR
dispatcher.register_callback_query_handler(
    tracks_similar, text_startswith="track__similar_"
)

# ADS
dispatcher.register_message_handler(
    menu_ads, text="/ads"
)

# Create AD
dispatcher.register_callback_query_handler(
    create_ad__start, text="ads__create_ad"
)
dispatcher.register_message_handler(
    create_ad__text, state=StateAD.text
)
dispatcher.register_message_handler(
    create_ad__button_title, state=StateAD.button_title
)
dispatcher.register_message_handler(
    create_ad__button_url, state=StateAD.button_url
)
dispatcher.register_message_handler(
    create_ad__view_limit, state=StateAD.view_limit
)
dispatcher.register_callback_query_handler(
    cancel_ad, state=StateAD, text="cancel_ad"
)
