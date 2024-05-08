from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

category_kb = ReplyKeyboardBuilder([
    [
        KeyboardButton(text="Участник шортлиста 📋"),
        KeyboardButton(text="Участник конкурса 🙋")
    ]
]).as_markup(resize_keyboard=True)
