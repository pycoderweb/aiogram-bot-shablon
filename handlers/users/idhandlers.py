from aiogram import Bot, Dispatcher, executor, types
from keyboards.default.menukeyboards import menu
from filters.search_quran import quran_uzb
import logging
from loader import dp

SUPERUSERS = [5770719103]
BLACKLIST = [123424,32456545]

@dp.message_handler(chat_id=5770719103,commands='start')
async def id_filter_example(msg:types.Message):
    await msg.answer('Xush kelibsiz superUser!',reply_markup=menu)