from aiogram.fsm.state import StatesGroup, State

class NominationState(StatesGroup):
    prose = State()
    poetry = State()