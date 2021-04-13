  
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor, callback_data
import yaml
from pprint import pprint
import time
import asyncio



def telegram():
    with open(f"/home/python/Documents/exp/my_pass.yaml") as f3:
        info = yaml.safe_load(f3)
        token = info['timer_bot']['token']
    bot = Bot(token=token)
    dp = Dispatcher(bot)
# MAIN function 
    #скачивает файл
    # any type messages handler
    @dp.message_handler(content_types=types.ContentType.ANY)
    async def catch_any(message: types.Message):
        if message.content_type == types.ContentType.DOCUMENT:
            await message.reply(f'Вы прислали  document')
            file_id = message.document.file_id
            file_info = await bot.get_file(file_id)
            downloaded_file = await bot.download_file(file_info.file_path)
            src = '/home/python/Documents/exp/' + file_id
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file.read())
                await message.reply(message, "Пожалуй, я сохраню это")
        if message.content_type == types.ContentType.TEXT:
            await message.reply(f'Вы прислали  only text')

        if message.content_type == types.ContentType.PHOTO:
            await message.reply(f'Вы прислали  photo')
            file_id = message.photo[-1].file_id
            file_info = await bot.get_file(file_id)
            downloaded_file = await bot.download_file(file_info.file_path)
            src = '/home/python/Documents/exp/' + file_id
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file.read())
                await message.reply(message, "Пожалуй, я сохраню это")

        if message.content_type == types.ContentType.VOICE:
            await message.reply(f'Вы прислали  voice')
            file_id = message.voice.file_id
            file_info = await bot.get_file(file_id)
            downloaded_file = await bot.download_file(file_info.file_path)
            src = '/home/python/Documents/exp/' + file_id
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file.read())
                await message.reply(message, "Пожалуй, я сохраню это")

        if message.content_type == types.ContentType.AUDIO:
            await message.reply(f'Вы прислали  audio')
            file_id = message.audio.file_id
            file_info = await bot.get_file(file_id)
            downloaded_file = await bot.download_file(file_info.file_path)
            src = '/home/python/Documents/exp/' + file_id
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file.read())
                await message.reply(message, "Пожалуй, я сохраню это")
        if message.content_type == types.ContentType.VIDEO:
            await message.reply(f'Вы прислали  video')
            file_id = message.video.file_id
            file_info = await bot.get_file(file_id)
            downloaded_file = await bot.download_file(file_info.file_path)
            src = '/home/python/Documents/exp/' + file_id
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file.read())
                await message.reply(message, "Пожалуй, я сохраню это")

    executor.start_polling(dp)
    

if __name__ == '__main__':
    telegram()
