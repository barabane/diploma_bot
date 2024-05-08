from aiogram import types
from keyboards import category_kb


async def start_handler(msg: types.Message):
    await msg.answer("Выберите категорию:", reply_markup=category_kb)
