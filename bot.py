
from asyncio import run as async_run
import nest_asyncio
from aiogram import executor

from handlers import dispatcher


if __name__ == "__main__":

    async def start_bot():
        nest_asyncio.apply()
        executor.start_polling(dispatcher=dispatcher, skip_updates=True)
    async_run( start_bot() )
