import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))


async def main():
    dp = Dispatcher()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main=main())
