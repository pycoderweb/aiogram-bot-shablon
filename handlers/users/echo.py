from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, CallbackQuery
from filters.search_quran import quran_uzb
import logging
from keyboards.inline.author_tarjima import authors
from loader import *

@dp.message_handler(text="oyatni izlash")
async def search_oyat(message:types.Message):
    await message.answer("kimni tarjimasi orqali izlashni hohlaysiz!",reply_markup=authors)
    await message.delete()

@dp.callback_query_handler(lambda c: c.data == 'uzb-alaaudeenmansou')
async def quran_tarjima(call:CallbackQuery):
    await call.answer("siz Alaaudeen Mansour tarjimasini tanladingiz\nistalgan sura va oyat raqamini kiriting ")
    return 'uzb-alaaudeenmansou'

@dp.callback_query_handler(lambda c: c.data =="uzb-alauddinmansour")
async def quran_tarjima(call:CallbackQuery):
    await call.answer("siz Alauddin Mansour tarjimasini tanladingiz\nistalgan sura va oyat raqamini kiriting ")
    return 'uzb-alauddinmansour'

@dp.callback_query_handler(lambda c: c.data =="uzb-muhammadsodikmu")
async def quran_tarjima(call:CallbackQuery):
    await call.answer("siz Muhammad Sodik Muhammad Yusuf tarjimasini tanladingiz\nistalgan sura va oyat raqamini kiriting ")
    return 'uzb-muhammadsodikmu'

@dp.message_handler()
async def echo(message: types.Message):
        sura = message.text.split(" ")[0]
        oyat = message.text.split(" ")[1]
        sura = int(sura)
        oyat = int(oyat)
        name = await quran_tarjima(message) # quran_tarjima funksiyasi ishga tushirildi
        print(name)
        url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{name}.json"
        natija = f"{name} tarjimasi:\n{sura} - sura ({oyat} - oyat) :\n{quran_uzb(sura, oyat, url.format(name))}"
        await message.answer(natija)
