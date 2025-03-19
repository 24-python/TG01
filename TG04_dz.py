import asyncio
from aiogram import Bot, Dispatcher, F, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN
import random
from gtts import gTTS
import os
from aiogram.enums import ContentType
from googletrans import Translator
import keyboard as kb


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart()) # простое привестсвие
async def start(message: Message):
    await message.answer('Hi! Я - БОТ', reply_markup=kb.main_dz)

@dp.message(F.text == 'Привет!') # команда на выборe
async def test_button(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message(F.text == 'Пока!') # команда на выборe
async def test_button(message: Message):
    await message.answer(f'Пока, {message.from_user.first_name}!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
