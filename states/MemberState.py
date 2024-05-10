from aiogram.fsm.state import StatesGroup, State


class MemberState(StatesGroup):
    member = State()
    shortlist = State()
