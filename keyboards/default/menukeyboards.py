from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="oyatni izlash"),
        ],
        [
            KeyboardButton(text="ortga"),
            KeyboardButton(text="Bosh sahifa"),
        ]
    ],
    resize_keyboard=True
)