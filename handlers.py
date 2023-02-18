
from aiogram.dispatcher.filters.builtin import \
    CommandStart, CommandHelp, IDFilter, IsReplyFilter, \
    ChatTypeFilter, ChatType

from tg import dispatcher
from main_menu import main_menu
from search import search, search_tracks
from filters import SearchFilter
from track import track


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