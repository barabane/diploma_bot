from aiogram import types
from aiogram.fsm.context import FSMContext
from states import MemberState
from keyboards import nomination_kb


async def member_handler(msg: types.Message, state: FSMContext):
    await state.set_state(MemberState.member)
    await state.set_data({"member": "member"})
    await msg.answer("Выберите номинацию:", reply_markup=nomination_kb)


async def shortlist_handler(msg: types.Message, state: FSMContext):
    await state.set_state(MemberState.shortlist)
    await state.set_data({"member": "shortlist"})
    await msg.answer("Выберите номинацию:", reply_markup=nomination_kb)
