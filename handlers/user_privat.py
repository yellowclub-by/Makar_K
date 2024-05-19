from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command

user_router = Router()


@user_router.message(CommandStart())
async def start_message(message: types.Message):
    await message.answer('Привет, это ботайфонов, по продаже  какую модель вы хотели бы купить?')


@user_router.message(Command('catalog'))
@user_router.message(F.text.lower() == 'меню')
async def catalog(message: types.Message):
    await message.answer('Каталог скоро будет добавлен')


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
    await message.answer('Пункты выдачи')


# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.text.lower() == 'доставка')
# @user_router.message(F.text.lower().contains('доставк'))
# @user_router.message(F.text.lower().startswith('как'))
# @user_router.message(F.text.lower().endswith('?'))
# @user_router.message(F.text.lower().startswith('как'), F.text.lower().endswith('?'))
# @user_router.message( (F.text.lower().contains('цен')) | (F.text.lower().contains('стоимост')) )
# @user_router.message()
# async def echo(message: types.Message):
#     await message.answer('сработал магический фильтр')
    # user_text = message.text
    # await message.answer(user_text)

