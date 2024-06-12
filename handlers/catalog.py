from aiogram import types, Router, F
from aiogram.types import FSInputFile

catalog_router = Router()


@catalog_router.message(F.text.lower() == 'iphone 13')
async def iphone_13(message: types.Message):
    photo = FSInputFile('img\catalog\iphone 13 bl.jpg')
    await message.answer_photo(photo, caption='iphone 13 - бюджетная, но до сих пор актуальная модель iphone с чипом '
                                              'Bionic A 15')


@catalog_router.message(F.text.lower() == 'iphone 13 pro')
async def iphone_13_pro(message: types.Message):
    photo = FSInputFile('img\catalog\iphone 13 pro.jpg')
    await message.answer_photo(photo, caption='iphone 13 pro - модель, в которой все еще нет DynamicIsland ')


@catalog_router.message(F.text.lower() == 'iphone 14')
async def iphone_14(message: types.Message):
    photo = FSInputFile('img\catalog\iphone_14_black.jpg')
    await message.answer_photo(photo, caption='iphone 14 - лучше, чем iphone 13 за счет большего количества '
                                              'оперативной памяти')


@catalog_router.message(F.text.lower() == 'iphone 14 pro')
async def iphone_14_pro(message: types.Message):
    photo = FSInputFile('img\catalog\iphone 14 pro.png')
    await message.answer_photo(photo, caption='iphone 14 pro - можно купить, если у вас не хватает денег на iphone 15 '
                                              'pro ')


@catalog_router.message(F.text.lower() == 'iphone 15')
async def iphone_15(message: types.Message):
    photo = FSInputFile('img\catalog\iphone 15.png')
    await message.answer_photo(photo, caption='iphone 15 - самый выгодный айфон для покупки в 2024 году')


@catalog_router.message(F.text.lower() == 'iphone 15 pro')
async def iphone_15_pro(message: types.Message):
    photo = FSInputFile('img\catalog\iphone 15 pro.jpg')
    await message.answer_photo(photo, caption='iphone 15 pro - модель, котора прослужит вам более 5 лет без неудобств')

