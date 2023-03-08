from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

@dp.message_handler(commands='state')
async def state_example(msg:types.Message,state:FSMContext):
    """Foydalanuvchi bir state ichiga o'tkazish"""
    await state.set_state('xarid qilish')
    await msg.answer("Mahsulot tanlang")

@dp.message_handler(state='xarid state')
async def state_example(msg:types.Message,state:FSMContext):
    await msg.answer("Mahsulot savatga qo'shildi")
    await state.finish()
    