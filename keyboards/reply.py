from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='каталог'),
            KeyboardButton(text='о нас')
        ],
        [
            KeyboardButton(text='контакты'),
            KeyboardButton(text='пункты выдачи')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Iphone manager'
)
catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='iphone 13'),
            KeyboardButton(text='iphone 13 pro')
        ],
        [
            KeyboardButton(text='iphone 14'),
            KeyboardButton(text='iphone 14 pro')
        ],
        [
            KeyboardButton(text='iphone 15'),
            KeyboardButton(text='iphone 15 pro')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Iphone manager'
)
