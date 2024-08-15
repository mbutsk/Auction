import logging
import asyncio
import sys
from aiogram import types, F
from aiogram.filters.command import Command
from aiogram.methods.delete_webhook import DeleteWebhook
from bot import dp, bot

# Code here

async def main() -> None:
# And the run events dispatching
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())