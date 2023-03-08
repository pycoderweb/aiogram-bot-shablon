from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_data import auhtor_callback


authors = InlineKeyboardMarkup(row_width=1)


authors_uz = {
    "Alaaudeen Mansour":"uzb-alaaudeenmansou",
    "Alauddin Mansour":"uzb-alauddinmansour",
    "Muhammad Sodik Muhammad Yusuf":"uzb-muhammadsodikmu"
 }

for ism,nom in authors_uz.items():
    authors.insert(InlineKeyboardButton(text=ism,callback_data=nom))

