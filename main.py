import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

# @dp.message(Command('photo', prefix='!')) # префикс перед командой
# async def photo(message: Message):
#     list = ['https://saltmag.ru/media/articles/inner/2020/6373/2_gIzSf7E.jpg',
#             'https://saltmag.ru/media/articles/inner/2020/6373/1_goqINJP.jpg',
#             'https://saltmag.ru/media/articles/inner/2020/6373/3_cRVfFCG.jpg'
#             ]
#     rand_photo = random.choice(list)
#     await message.answer_photo(photo=rand_photo, caption='Супер фотка')

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://saltmag.ru/media/articles/inner/2020/6373/2_gIzSf7E.jpg',
            'https://saltmag.ru/media/articles/inner/2020/6373/1_goqINJP.jpg',
            'https://saltmag.ru/media/articles/inner/2020/6373/3_cRVfFCG.jpg'
            ]
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Супер фотка')

@dp.message(F.photo)
async def photo(message: Message):
    list = ['Ого, какая фотка!', 'Не отправляй мне такого больше', 'Класс', 'Супер']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

@dp.message(F.text == 'Что такое ИИ?')
async def aitext(message: Message):
    await message.answer('Искусственный интеллект (ИИ) — это технология, которая позволяет машинам демонстрировать человекоподобные рассуждения и возможности, такие как автономное принятие решений.')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start - запуск бота \n /help - помощь')

# @dp.message(CommandStart()) # простое привестсвие
# async def start(message: Message):
#     await message.answer('Hi! Я - БОТ')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Hi, {message.from_user.first_name}') # привестсвие с именем

@dp.message()
async def start(message: Message):
    await message.send_copy(chat_id=message.chat.id)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


