import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from handlers import start_handler

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))


async def main():
    dp = Dispatcher()
    dp.message.register(start_handler, CommandStart())

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main=main())
