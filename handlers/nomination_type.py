from aiogram import types
from aiogram.fsm.context import FSMContext
from states import NominationState


async def prose_handler(msg: types.Message, state: FSMContext):
    await state.set_state(NominationState.prose)
    await state.update_data({"nomination": "prose"})
    await msg.answer("Введите ваши фамилию и имя:")


async def poetry_handler(msg: types.Message, state: FSMContext):
    await state.set_state(NominationState.poetry)
    await state.update_data({"nomination": "poetry"})
    await msg.answer("Введите ваши фамилию и имя:")
