from aiogram import types, Router, F

group_router = Router()

ban_words = ['samsung', 'xiomi', 'vivo', 'huawei', 'android', 'honor', 'poco', 'realme', 'google', 'infinix', 'oneplus']


@group_router.message(F.text)
async def cleaner(message: types.Message):
    words_lst = message.text.split(' ')
    for word in words_lst:
        if word.lower() in ban_words:
            await message.answer(f'Пожалуйста соблюдайте правила чата!!! {message.from_user.first_name}!')
            await message.delete()
            break










