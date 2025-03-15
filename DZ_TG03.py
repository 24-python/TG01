import asyncio
import sqlite3
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import STUD_TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=STUD_TOKEN)
dp = Dispatcher()

# Определение состояний
class Form(StatesGroup):
    name = State()
    age = State()
    grade = State()

# Функция для инициализации базы данных
def init_db():
    conn = sqlite3.connect("school_data.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )""")
    conn.commit()
    conn.close()

# Инициализация базы данных перед запуском бота
init_db()

# Обработчик команды /start
@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Привет! Как тебя зовут?")
    await state.set_state(Form.name)

# Обработчик имени
@dp.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Сколько тебе лет?")
    await state.set_state(Form.age)

# Обработчик возраста
@dp.message(Form.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введи свой возраст цифрами.")
        return
    await state.update_data(age=int(message.text))
    await message.answer("В каком классе ты учишься?")
    await state.set_state(Form.grade)

# Обработчик класса и сохранение в БД
@dp.message(Form.grade)
async def process_grade(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    user_data = await state.get_data()

    # Сохранение в базу данных
    conn = sqlite3.connect("school_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
                   (user_data["name"], user_data["age"], user_data["grade"]))
    conn.commit()
    conn.close()

    # Отправляем подтверждение пользователю
    await message.answer(f"Спасибо, {user_data['name']}! Твои данные сохранены:\n"
                         f"Возраст: {user_data['age']}\n"
                         f"Класс: {user_data['grade']}")

    # Завершаем FSM
    await state.clear()

# Функция запуска бота
async def main():
    await dp.start_polling(bot)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
