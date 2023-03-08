from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.menukeyboards import menu

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.reply(f"Assalomu alaykum va rahmatullohu barakotuh {message.from_user.full_name}",reply_markup=menu)

