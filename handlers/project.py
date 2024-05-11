from aiogram import types
from aiogram.fsm.context import FSMContext


async def project_handler(msg: types.Message, state: FSMContext):
    await state.update_data({"project": msg.text.lower().title()})
    data = await state.get_data()
