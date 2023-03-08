from aiogram import Bot, Dispatcher, executor, types

from filters.search_quran import quran_uzb
import logging
from loader import dp

@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
@dp.message_handler(content_types='photo')
async def photo_handler(msg:types.Message):
    await msg.answer("vooo, kimni rasmi bu")