# Напишите код для сохранения всех фото, которые отправляет пользователь боту в папке img
@dp.message(F.photo)
async def photo(message: Message): # обработка фоток и скачивание их на комп в папку img
   await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')

#Отправьте с помощью бота голосовое сообщение

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

# Напишите код для перевода любого текста, который пишет пользователь боту, на английский язык

translator = Translator()
@dp.message()
async def translate_message(message: Message):
    # Перевод сообщения
    translated_text = translator.translate(message.text, src="ru", dest="en").text

    # Отправка переведенного текста
    await message.answer(f"In English: {translated_text}")
