import os
from aiogram import types
from aiogram.fsm.context import FSMContext
from utils import create_diploma
from keyboards import category_kb


async def project_handler(msg: types.Message, state: FSMContext):
    await state.update_data({"project": msg.text})
    user_data = await state.get_data()

    if user_data["member"] == "member" and user_data["nomination"] == "prose":
        diploma = create_diploma("static/1.png", user_data)
        await msg.answer("Формируем диплом...")
        await msg.answer_photo(types.FSInputFile(f"static/{diploma}"), reply_markup=category_kb)
        os.remove(f"static/{diploma}")
    elif user_data["member"] == "member" and user_data["nomination"] == "poetry":
        diploma = create_diploma("static/2.png", user_data)
        await msg.answer("Формируем диплом...")
        await msg.answer_photo(types.FSInputFile(f"static/{diploma}"), reply_markup=category_kb)
        os.remove(f"static/{diploma}")
    elif user_data["member"] == "shortlist" and user_data["nomination"] == "poetry":
        diploma = create_diploma("static/3.png", user_data)
        await msg.answer("Формируем диплом...")
        await msg.answer_photo(types.FSInputFile(f"static/{diploma}"), reply_markup=category_kb)
        os.remove(f"static/{diploma}")
    elif user_data["member"] == "shortlist" and user_data["nomination"] == "prose":
        diploma = create_diploma("static/4.png", user_data)
        await msg.answer("Формируем диплом...")
        await msg.answer_photo(types.FSInputFile(f"static/{diploma}"), reply_markup=category_kb)
        os.remove(f"static/{diploma}")
