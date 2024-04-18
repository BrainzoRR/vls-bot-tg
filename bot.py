from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7129364747:AAFe0pejlCUzTqmNXE5HL8QT9R3YFVO3PH0')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Нажми', web_app=WebAppInfo))
    await message.answer('Слава VLS', reply_markup=markup)