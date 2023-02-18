
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

import message_texts


class SearchFilter(BoundFilter):
    async def check(self, update: Message) -> bool:
        try:
            if update.reply_to_message.text == message_texts.SEARCH:
                return True
        except AttributeError:
            pass
        return False
