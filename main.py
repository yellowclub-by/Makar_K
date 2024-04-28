import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = '6623672582:AAEBMDrhc5ncnF7CtwFsVgscYasmW8O6oCU'

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_message(message: types.message):
    await message.answer('Привет, это бот по продаже айфонов, какую модель вы хотели бы купить?')


@dp.message()
async def echo(message: types.message):
    await message.answer('бот пока что  находится в разработке')
    user_text = message.text
    await message.answer(user_text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
