from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Тестовая кнопка 1')],
    [KeyboardButton(text='Тестовая кнопка 2'), KeyboardButton(text='Тестовая кнопка 3')],
], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Новости', callback_data='news')],
    [InlineKeyboardButton(text='Профиль', callback_data='person')]
])

test = ['кнопка 1', 'кнопка 2', 'кнопка 3', 'кнопка 4']

async def test_keyboard():
    keyboard = ReplyKeyboardBuilder()
    for key in test:
        keyboard.add(KeyboardButton(text=key))
    return keyboard.adjust(2).as_markup()


async def test_inline_keyboard():
    inline_keyboard = InlineKeyboardBuilder()
    for key in test:
        inline_keyboard.add(InlineKeyboardButton(text=key, url='https://google.com'))
    return inline_keyboard.adjust(2).as_markup()

main_dz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Привет!'), KeyboardButton(text='Пока!')],
], resize_keyboard=True)

inline_keyboard_dz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Новости', url='https://google.com/news')],
    [InlineKeyboardButton(text='Музыка', url='https://google.com/music')],
    [InlineKeyboardButton(text='Видео', url='https://google.com/video')]
    ])

# Клавиатура с кнопкой "Показать больше"
def get_show_more_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
    ])

# Клавиатура с кнопками "Опция 1" и "Опция 2"
def get_options_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
        [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
    ])