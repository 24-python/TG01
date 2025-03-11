import asyncio
import requests
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN_weather, OPENWEATHER_API_KEY

bot = Bot(token=TOKEN_weather)
dp = Dispatcher()


# Функция для получения погоды
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},RU&appid={OPENWEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"].capitalize()

        return f"🌡 Температура: {temperature}°C\n💧 Влажность: {humidity}%\n☁️ Погода: {weather_desc}"
    elif response.status_code == 404:
        return "❌ Город не найден. Проверьте правильность написания!"
    else:
        return "⚠️ Ошибка сервера. Попробуйте позже."


# Команда /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Я - бот, выдающий прогноз погоды. Введи команду /weather для получения прогноза.")


# Команда /help
@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Я умею выполнять команды:\n/start - запуск бота\n/help - помощь\n/weather - прогноз погоды")


# Команда /weather
@dp.message(Command("weather"))
async def ask_city(message: Message):
    await message.answer("Введите название города:")


# Обработчик ввода города
@dp.message(F.text)
async def send_weather(message: Message):
    city = message.text.strip()
    weather_info = get_weather(city)
    await message.answer(weather_info)


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
