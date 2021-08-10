# python bot.py
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from config import TOKEN
import markups as nav
import base
import random
import asyncio

# Configure logging (info about bot in terminal)
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# This handler will be called when user sends `/start` or `/help` command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, '🍓Meow (Привет), {0.first_name}🍓 \nЯ попал на землю недавно, но уже вижу, кто тут сладкий пирожочек (ты)\nЧем сегодня займёмся?🌼'.format(message.from_user),reply_markup = nav.mainMenu)

# help command
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'Meow \nДержи меню: '.format(message.from_user),reply_markup = nav.mainMenu)

# sms for sms
@dp.message_handler()
async def echo(message: types.Message):
    # await message.answer(message.text)
    if message.text == 'Вселенная':
        await bot.send_message(message.from_user.id, 'Посмотри, как тут интересно!', reply_markup = nav.Menu)
    elif message.text == 'Рандомное число':
        await bot.send_message(message.from_user.id, 'Вселенная думает, что предназначенное тебе число...\n🌼' + str(random.randint(1, 9999)))
    elif message.text == 'Отдел информации':
        await bot.send_message(message.from_user.id, 'и что вы все надеетесь тут найти?')
    elif message.text == 'Планета Флопп':
        await bot.send_photo(message.from_user.id, base.FLOPPA[int(random.randint(0,len(base.FLOPPA)-1))],
                             reply_to_message_id=message.message_id)

    elif message.text == 'КотоМир':
        await bot.send_photo(message.from_user.id, base.KITTENS[int(random.randint(0,2))],
                             reply_to_message_id=message.message_id)

    elif message.text == 'Планета милых видео':
            user_id = message.from_user.id
            await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO_NOTE)
            await asyncio.sleep(1)  # конвертируем видео и отправляем его пользователю
            await bot.send_video_note(message.from_user.id, base.VIDEO_NOTE)

    elif message.text == 'Планета мультиков':
        await bot.send_message(message.from_user.id, 'мур')

    else:
        await bot.send_message(message.from_user.id, 'Зачем писать другие команды? Посмотри список!',  reply_markup=nav.mainMenu)




# длинный опрос
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
