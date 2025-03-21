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

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()


@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('video.mp4')
    await bot.send_video(message.chat.id, video)

@dp.message(Command('voice'))
async def voice(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_voice')
    voice = FSInputFile('voice.ogg')
    await message.answer_voice(voice)

@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile('doc.pdf')
    await bot.send_document(message.chat.id, doc)

@dp.message(Command('audio'))
async def audio(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_audio')
    audio = FSInputFile('audio.mp3')
    await bot.send_audio(message.chat.id, audio)

@dp.message(Command('training'))
async def training(message: Message):
    training_list = [
        "Тренировка 1:\n1. Скручивания: 3 подхода по 15 повторений\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\n3. Планка: 3 подхода по 30 секунд",
        "Тренировка 2:\n1. Подъемы ног: 3 подхода по 15 повторений\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
        "Тренировка 3:\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
    ]

    rand_tr = random.choice(training_list)

    await message.answer(f"Это ваша минитренировка на сегодня: {rand_tr}")
    tts = gTTS(text=rand_tr, lang='ru')
    tts.save('training.ogg')
    voice = FSInputFile('training.ogg')
    await bot.send_voice(message.chat.id, voice)
    os.remove('training.ogg')


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
# async def photo(message: Message):
#     list = ['Ого, какая фотка!', 'Не отправляй мне такого больше', 'Класс', 'Супер']
#     rand_answ = random.choice(list)
#     await message.answer(rand_answ)

@dp.message(F.photo)
async def photo(message: Message): # обработка фоток и скачивание их на комп в папку tmp
    list = ['Ого, какая фотка!', 'Не отправляй мне такого больше', 'Класс', 'Супер']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')

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

#Напишите код для перевода любого текста, который пишет пользователь боту, на английский язык
@dp.message()
async def translate_message(message: Message):
    # Перевод сообщения
    translated_text = translator.translate(message.text, src="ru", dest="en").text

    # Отправка переведенного текста
    await message.answer(f"In English: {translated_text}")

# @dp.message()
# async def start(message: Message):
#     await message.send_copy(chat_id=message.chat.id)

@dp.message()
async def echo_and_voice(message: Message):
    # Отправка копии текстового сообщения
    await message.send_copy(chat_id=message.chat.id)

    if not message.text.strip():  # Проверяем, есть ли текст
        return

    # Создание голосового сообщения
    tts = gTTS(text=message.text, lang='ru')
    tts.save('message.ogg')
    voice = FSInputFile('message.ogg')

    # Отправка голосового сообщения
    await bot.send_voice(chat_id=message.chat.id, voice=voice)

    # Удаление файла
    os.remove('message.ogg')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


