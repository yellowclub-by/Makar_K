from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def adresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
InlineKeyboardButton(text='улица Солтыса 56-72, Минск', callback_data='addresses_1'),
        InlineKeyboardButton(text='проспект Победителей', callback_data='addresses_2'),
        width=1
     )
    return builder.as_markup()


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Site', url='https://www.apple.com/'),
            InlineKeyboardButton(text='Telegram', url='tg://resolve?domain=iphone')
        ]
    ]
)



