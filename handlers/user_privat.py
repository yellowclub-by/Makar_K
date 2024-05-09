from aiogram import types, Router
from aiogram.filters import CommandStart, Command


user_router = Router()


@user_router.message(CommandStart())
async def start_message(message: types.message):
    await message.answer('Привет, это бот по продаже айфонов, какую модель вы хотели бы купить?')


@user_router.message(Command('catalog'))
async def catalog(message: types.message):
    await message.answer('Каталог скоро будет добавлен')


@user_router.message(Command('about'))
async def about(message: types.message):
    await message.answer('Мы подберем для вас айфон по выгодной цене')


@user_router.message(Command('contacts'))
async def contacts(message: types.message):
    await message.answer('Позже здесь будут номера спонсоров')


@user_router.message(Command('addresses'))
async def addresses(message: types.message):
    await message.answer('Адрес')


@user_router.message()
async def echo(message: types.message):
    await message.answer('бот пока что  находится в разработке')
    user_text = message.text
    await message.answer(user_text)






