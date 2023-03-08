from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards.default.menukeyboards import menu
from loader import dp

@dp.message_handler(Text(equals="Assalomu alaykum!",ignore_case=True))
async def text_example(msg:types.Message):
    await msg.reply("Va alaykum Assalom")

@dp.message_handler(Text(contains="assalom",ignore_case=True))
async def text_example(msg:types.Message):
    await msg.reply("Va alaykum Assalom")

@dp.message_handler(text_contains="ortga")
async def back_page(msg:types.Message):
    await msg.reply("siz bir marta orqaga qaytdingiz")

@dp.message_handler(text_contains="Bosh sahifa")
async def home_page(ms:types.Message):
    await ms.answer("assalomu alaykum tanlang",reply_markup=menu)