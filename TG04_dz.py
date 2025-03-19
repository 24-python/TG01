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


@dp.message(CommandStart())  # Простое приветствие
async def start(message: Message):
    await message.answer('Hi! Я - БОТ', reply_markup=kb.main_dz)

@dp.message(F.text.in_(['Привет!', 'Пока!']))  # Обработка команд "Привет!" и "Пока!"
async def handle_greetings(message: Message):
    if message.text == 'Привет!':
        await message.answer(f'Привет, {message.from_user.first_name}!')
    elif message.text == 'Пока!':
        await message.answer(f'Пока, {message.from_user.first_name}!')

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer('Свежий контент только для тебя', reply_markup=kb.inline_keyboard_dz)

@dp.message(Command("dynamic"))
async def cmd_dynamic(message: types.Message):
    # Получаем клавиатуру с кнопкой "Показать больше"
    keyboard = kb.get_show_more_keyboard()
    await message.answer("Нажмите на кнопку ниже:", reply_markup=keyboard)

# Обработчик нажатия на инлайн-кнопку "Показать больше"
@dp.callback_query(lambda c: c.data == "show_more")
async def show_more_options(callback: types.CallbackQuery):
    # Получаем клавиатуру с кнопками "Опция 1" и "Опция 2"
    keyboard = kb.get_options_keyboard()
    # Редактируем сообщение, заменяя кнопку
    await callback.message.edit_text("Выберите опцию:", reply_markup=keyboard)
    await callback.answer()

# Обработчик нажатия на "Опция 1" или "Опция 2"
@dp.callback_query(lambda c: c.data in ["option_1", "option_2"])
async def handle_option(callback: types.CallbackQuery):
    option_text = "Вы выбрали Опцию 1" if callback.data == "option_1" else "Вы выбрали Опцию 2"
    await callback.message.answer(option_text)
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
