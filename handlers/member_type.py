from aiogram import types
from aiogram.fsm.context import FSMContext
from states import MemberState


async def member_handler(msg: types.Message, state: FSMContext):
    await state.set_state(MemberState.member)
    await msg.answer("Напишите свое имя и фамилию:")


async def shortlist_handler(msg: types.Message, state: FSMContext):
    await state.set_state(MemberState.shortlist)
    await msg.answer("Напишите свое имя и фамилию:")
