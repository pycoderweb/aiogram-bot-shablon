from aiogram import Bot, Dispatcher, executor, types

from filters.search_quran import quran_uzb
import logging
from loader import dp

@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['eur','usd'])
async def hashtag_example(msg:types.Message):
    await msg.answer("yeee,akang kuchaydi!")
