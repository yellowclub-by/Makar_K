from aiogram import types, Router, F
from aiogram.types import FSInputFile

catalog_router = Router()


@catalog_router.message(F.text.lower() == 'iphone 13')
async def iphone_13(message: types.Message):
    photo = FSInputFile('img\catalog\iphone 13 bl.jpg')
    await message.answer_photo(photo, caption='''<b>iPhone 13</b>
                    \nБюджетная, но до сих пор актуальная модель iphone с чипом Bionic A 15, вы можете купить его здесь: 
https://gsmarena.by/catalog/apple-iphone-13.html ''' )


@catalog_router.message(F.text.lower() == 'iphone 13 pro')
async def iphone_13_pro(message: types.Message):
    photo = FSInputFile('img\catalog\iphone 13 pro.jpg')
    await message.answer_photo(photo, caption='''<b>iPhone 13 Pro</b>
                    \nМодель, в которой все еще нет DynamicIsland, вы можете купить его здесь:
https://gsmarena.by/catalog/apple-iphone-13-pro.html ''')


@catalog_router.message(F.text.lower() == 'iphone 14')
async def iphone_14(message: types.Message):
    photo = FSInputFile('img\catalog\iphone_14_black.jpg')
    await message.answer_photo(photo, caption='''<b>iPhone 14</b> 
                    \nЛучше, чем iphone 13 за счет большего количества оперативной памяти, вы можете купить его здесь: 
https://gsmarena.by/catalog/iphone-14.html''')


@catalog_router.message(F.text.lower() == 'iphone 14 Pro')
async def iphone_14_pro(message: types.Message):
    photo = FSInputFile('img\catalog\iphone 14 pro.png')
    await message.answer_photo(photo, caption='''<b>iPhone 14 pro</b> 
                    \nМожно купить, если у вас не хватает денег на iphone 15 pro, вы можете купить его здесь:
https://gsmarena.by/catalog/iphone-14-pro.html ''')


@catalog_router.message(F.text.lower() == 'iphone 15')
async def iphone_15(message: types.Message):
    photo = FSInputFile('img\catalog\iphone 15.png')
    await message.answer_photo(photo, caption='''<b>iPhone 15</b> 
                        \nCамый выгодный айфон для покупки в 2024 году, вы можете купить его здесь:
https://gsmarena.by/catalog/apple-iphone-15-128gb.html''')



@catalog_router.message(F.text.lower() == 'iphone 15 Pro')
async def iphone_15_pro(message: types.Message):
    photo = FSInputFile('img\catalog\iphone 15 pro.jpg')
    await message.answer_photo(photo, caption='''<b>iPhone 15 pro</b> 
                        \nМодель, которая прослужит вам более 5 лет без неудобств, вы можете купить его здесь:
https://gsmarena.by/catalog/apple-iphone-15-pro-128gb.html''')


