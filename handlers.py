
from aiogram.dispatcher.filters.builtin import \
    CommandStart, CommandHelp, IDFilter, IsReplyFilter, \
    ChatTypeFilter, ChatType

from tg import dispatcher
from main_menu import main_menu


# MAIN MENU
dispatcher.register_message_handler(
    main_menu, ChatTypeFilter(chat_type=ChatType.PRIVATE), CommandStart()
)