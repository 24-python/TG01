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

@dp.callback_query(F.data == 'news')
async def news(callback: types.CallbackQuery):
    await callback.answer('Новости подгружаются...', show_alert=True)
    await callback.message.edit_text('Вот свежие новости', reply_markup=await kb.test_inline_keyboard())

@dp.message(F.text == 'Тестовая кнопка 1') # команда на выборe
async def test_button(message: Message):
    await message.answer('Это обработка нажатия reply-кнопок')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start - запуск бота \n /help - помощь')


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Hi, {message.from_user.first_name}', reply_markup=kb.inline_keyboard_test) # привестсвие с именем

#

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


