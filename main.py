# SO2 SCAM BOT BY github.com/Vlad2030

import os
import asyncio
import random
# Импорт .py кода
import donate
import text
import keyboard

# Импорт фреймворков
try:
    from aiogram import Bot, Dispatcher, executor, types
except ImportError:
    os.system('pip install -r requirements.txt')

# Авторизация бота
bot = Bot(token='ваш токен', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

random_id = random.randint(10000, 99999)

# /start
@dp.message_handler(commands=['start'])
async def Start(message: types.Message):
    await message.answer(text.main_text, reply_markup=keyboard.BuyKeyboard())

# Callback Купить на сутки
@dp.callback_query_handler(text="callback_buy1")
async def CallbackBuy1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(message_id=callback_query.message.message_id, chat_id=callback_query.message.chat.id, text=f'{text.buy_text}<code>{random_id}:{text.buy1_cash}</code>', reply_markup=keyboard.Buy1LinkKeyboard())

# Callback Купить на неделю
@dp.callback_query_handler(text="callback_buy2")
async def CallbackBuy2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(message_id=callback_query.message.message_id, chat_id=callback_query.message.chat.id, text=f'{text.buy_text}<code>{random_id}:{text.buy2_cash}</code>', reply_markup=keyboard.Buy2LinkKeyboard())

# Callback Купить на месяц
@dp.callback_query_handler(text="callback_buy3")
async def CallbackBuy3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(message_id=callback_query.message.message_id, chat_id=callback_query.message.chat.id, text=f'{text.buy_text}<code>{random_id}:{text.buy3_cash}</code>', reply_markup=keyboard.Buy3LinkKeyboard())

# Callback Купить наавсегда
@dp.callback_query_handler(text="callback_buy4")
async def CallbackBuy4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(message_id=callback_query.message.message_id, chat_id=callback_query.message.chat.id, text=f'{text.buy_text}<code>{random_id}:{text.buy4_cash}</code>', reply_markup=keyboard.Buy4LinkKeyboard())

@dp.callback_query_handler(text="callback_menu")
async def CallbackMenu(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(message_id=callback_query.message.message_id, chat_id=callback_query.message.chat.id, text=text.main_text, reply_markup=keyboard.BuyKeyboard())

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)