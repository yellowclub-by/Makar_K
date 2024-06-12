from keyboards import reply, inline
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command

user_router = Router()


@user_router.message(CommandStart())
async def start_message(message: types.Message):
    await message.answer('Привет, это бот по продаже айфонов, какую модель вы хотели бы купить?',
                         reply_markup=reply.start_kb)


@user_router.message(Command('catalog'))
@user_router.message(F.text.lower() == 'каталог')
async def catalog(message: types.Message):
    await message.answer('Вот айфоны, которые сейчас в наличии', reply_markup=reply.catalog_kb)


@user_router.message(Command('about'))
@user_router.message(F.text.lower() == 'о нас')
async def about(message: types.Message):
    await message.answer('Мы подберем нужный вам айфон по выгодной цене')


@user_router.message(Command('contacts'))
@user_router.message(F.text.lower() == 'контакты')
async def contacts(message: types.Message):
    await message.answer('Позже здесь будут номера спонсоров')


@user_router.message(Command('addresses'))
@user_router.message(F.text.lower() == 'пункты выдачи')
async def addresses(message: types.Message):
    await message.answer('Пункты выдачи', reply_markup=inline.adresses_kb())


@user_router.callback_query(F.data.lower().startswith('addresses'))
async def addresses_types(callback: types.CallbackQuery):
    query = callback.data.split('_')[1]
    if query == '1':
        await callback.message.answer('это первый пункт выдачи')
    elif query == '2':
        await callback.message.answer('это второй пункт выдачи')
    elif query == '3':
        await callback.message.answer('это третий пункт выдачи')
    elif query == '4':
        await callback.message.answer('это четвертый пункт выдачи')
    await callback.answer()



@user_router.message(F.text.lower() == 'назад')
async def back_menu(message: types.Message):
    await message.answer('Главное меню', reply_markup=reply.start_kb)






# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.text.lower() == 'доставка')
# @user_router.message(F.text.lower().contains('доставк'))
# @user_router.message(F.text.lower().startswith('как'))
# @user_router.message(F.text.lower().endswith('?'))
# @user_router.message(F.text.lower().startswith('как'), F.text.lower().endswith('?'))
# @user_router.message( (F.text.lower().contains('цен')) | (F.text.lower().contains('стоимость')) )
# @user_router.message()
# async def echo(message: types.Message):
#     await message.answer('сработал магический фильтр')
# user_text = message.text
# await message.answer(user_text)
