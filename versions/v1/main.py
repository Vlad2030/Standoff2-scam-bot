# SO2 SCAM BOT BY github.com/Vlad2030


# import frameworks
try:
    import os
    import asyncio
    import random
    from loguru import logger
    from aiogram import Bot, Dispatcher, executor, types
    logger.add("logs.log", enqueue=False, backtrace=False, catch=False)
    logger.info('importing frameworks..')
except Exception as excp:
    logger.error('{excp}! trying install..', excp=excp)
    os.system("pip install -r requirements.txt")
finally:
    logger.success('frameworks imported!')


# Импорт .py кода
from modules import donate
from modules import text
from modules import keyboards
from modules import bot_token


# Авторизация бота
bot = Bot(
    token=bot_token.TOKEN,
    parse_mode=types.ParseMode.HTML,
)
dp = Dispatcher(bot)


# /start
@dp.message_handler(commands="start")
async def Start(message: types.Message):
    logger.info(
        "/start from {user_id} id",
        user_id=message.from_user.id
    )
    await message.answer(
        text.main_text,
        reply_markup=keyboards.BuyKeyboard()
    )
    return None


# Callback Купить на сутки
@dp.callback_query_handler(text="callback_buy1")
async def CallbackBuy1(callback_query: types.CallbackQuery):
    logger.info(
        "callback_buy1 from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=f"{text.buy_text}<code>{callback_query.id}:{text.buy1_cash}</code>",
        reply_markup=keyboards.Buy1LinkKeyboard()
    )
    return None


# Callback Купить на неделю
@dp.callback_query_handler(text="callback_buy2")
async def CallbackBuy2(callback_query: types.CallbackQuery):
    logger.info(
        "callback_buy2 from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=f"{text.buy_text}<code>{callback_query.id}:{text.buy2_cash}</code>",
        reply_markup=keyboards.Buy2LinkKeyboard()
    )
    return None


# Callback Купить на месяц
@dp.callback_query_handler(text="callback_buy3")
async def CallbackBuy3(callback_query: types.CallbackQuery):
    logger.info(
        "callback_buy3 from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=f"{text.buy_text}<code>{callback_query.id}:{text.buy3_cash}</code>",
        reply_markup=keyboards.Buy3LinkKeyboard()
    )
    return None


# Callback Купить наавсегда
@dp.callback_query_handler(text="callback_buy4")
async def CallbackBuy4(callback_query: types.CallbackQuery):
    logger.info(
        "callback_buy4 from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=f"{text.buy_text}<code>{callback_query.id}:{text.buy4_cash}</code>",
        reply_markup=keyboards.Buy4LinkKeyboard()
    )
    return None


@dp.callback_query_handler(text="callback_menu")
async def CallbackMenu(callback_query: types.CallbackQuery):
    logger.info(
        "callback_menu from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.main_text,
        reply_markup=keyboards.BuyKeyboard()
    )
    return None


# Запуск бота
if __name__ == "__main__":
    logger.success('bot started')
    executor.start_polling(dp, skip_updates=True)
    logger.warning('bot shutdown!')