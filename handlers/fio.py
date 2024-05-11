from aiogram import types
from aiogram.fsm.context import FSMContext
from states import FioState
from keyboards import category_kb


async def fio_handler(msg: types.Message, state: FSMContext):
    await state.set_state(FioState.fio)
    await state.update_data({"fio": msg.text.lower().title()})
    await msg.answer("Напишите название вашей работы:", reply_markup=category_kb.one_time_keyboard)
