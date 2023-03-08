from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
COMMAND_EMAIL_REGEX = r'/email:'+EMAIL_REGEX
@dp.message_handler(filters.Regexp(EMAIL_REGEX))
async def email_regex_example(msg:types.Message):
    await msg.reply("Siz email yubordiniz")