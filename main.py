# SO2 SCAM BOT BY github.com/Vlad2030

# Импорт фреймворков
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging

# Импорт .py кода
import api as api
import donation_alerts as donationalerts
import texts as text

# Авторизация бота
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api.API_ID, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# /start
@dp.message_handler(commands=['start'])
async def Start(message: types.Message):
    message_photo = open('Logo_og.jpg', 'rb')
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text=text.buy1_keyboard_text, callback_data='callback_buy1'))
    keyboard.add(types.InlineKeyboardButton(text=text.buy2_keyboard_text, callback_data='callback_buy2'))
    keyboard.add(types.InlineKeyboardButton(text=text.buy3_keyboard_text, callback_data='callback_buy3'))
    keyboard.add(types.InlineKeyboardButton(text=text.buy4_keyboard_text, callback_data='callback_buy4'))
    await message.reply_photo(message_photo, text.main_text, reply_markup = keyboard)

# Callback Купить на сутки
@dp.callback_query_handler(text="callback_buy1")
async def CallbackBuy1(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text=text.buy1_keyboard_text, url=donationalerts.DonationAlerts_Link))
    await bot.send_message(message.from_user.id, f'{text.buy_text}<code>{message.from_user.id}:{text.buy1_cash}</code>')
    await bot.send_message(message.from_user.id, text.donate_text, reply_markup = keyboard)

# Callback Купить на неделю
@dp.callback_query_handler(text="callback_buy2")
async def CallbackBuy2(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text=text.buy2_keyboard_text, url=donationalerts.DonationAlerts_Link))
    await bot.send_message(message.from_user.id, f'{text.buy_text}<code>{message.from_user.id}:{text.buy2_cash}</code>')
    await bot.send_message(message.from_user.id, text.donate_text, reply_markup = keyboard)

# Callback Купить на месяц
@dp.callback_query_handler(text="callback_buy3")
async def CallbackBuy3(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text=text.buy3_keyboard_text, url=donationalerts.DonationAlerts_Link))
    await bot.send_message(message.from_user.id, f'{text.buy_text}<code>{message.from_user.id}:{text.buy3_cash}</code>')
    await bot.send_message(message.from_user.id, text.donate_text, reply_markup = keyboard)

# Callback Купить наавсегда
@dp.callback_query_handler(text="callback_buy4")
async def CallbackBuy4(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text=text.buy4_keyboard_text, url=donationalerts.DonationAlerts_Link))
    await bot.send_message(message.from_user.id, f'{text.buy_text}<code>{message.from_user.id}:{text.buy4_cash}</code>')
    await bot.send_message(message.from_user.id, text.donate_text, reply_markup = keyboard)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)