from aiogram import types
from aiogram.fsm.context import FSMContext
from states import NominationState
from keyboards import nomination_kb


async def prose_handler(msg: types.Message, state: FSMContext):
    await state.set_state(NominationState.prose)
    await state.set_data({"nomination": "prose"})
    await msg.answer("Выберите номинацию:", reply_markup=nomination_kb)


async def poetry_handler(msg: types.Message, state: FSMContext):
    await state.set_state(NominationState.poetry)
    await state.set_data({"nomination": "poetry"})
    await msg.answer("Выберите номинацию:", reply_markup=nomination_kb)
