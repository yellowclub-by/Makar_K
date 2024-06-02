import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = '6623672582:AAEBMDrhc5ncnF7CtwFsVgscYasmW8O6oCU'

bot = Bot(token=TOKEN)
dp = Dispatcher()


from handlers.user_privat import user_router
from handlers.catalog import catalog_router

from handlers.user_group import group_router


dp.include_router(user_router)
dp.include_router(catalog_router)
dp.include_router(group_router)



async def main():
    await dp.start_polling(bot)


asyncio.run(main())
