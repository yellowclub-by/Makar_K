from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def adresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
InlineKeyboardButton(text='пункт выдачи №1', callback_data='addresses_1'),
        InlineKeyboardButton(text='пункт выдачи №2', callback_data='addresses_2'),
        InlineKeyboardButton(text='пункт выдачи №3', callback_data='addresses_3'),
        InlineKeyboardButton(text='пункт выдачи №4', callback_data='addresses_4'),
        width=2
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



