from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

nomination_kb = ReplyKeyboardBuilder([
    [
        KeyboardButton(text="Поэзия"),
        KeyboardButton(text="Проза")
    ]
]).as_markup(resize_keyboard=True)
