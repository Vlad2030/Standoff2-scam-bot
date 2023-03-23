# SO2 SCAM BOT BY github.com/Vlad2030

from aiogram import types
from loguru import logger

from keyboards import keyboard
from loader import dp
from modules import text


# Callback Купить на сутки
@dp.callback_query_handler(text="callback_buy1")
async def CallbackBuy1(callback_query: types.CallbackQuery) -> None:
    logger.info(
        "callback_buy1 from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await callback_query.bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=f"{text.buy_text}<code>{callback_query.id}:{text.buy1_cash}</code>",
        reply_markup=keyboard.Buy1LinkKeyboard()
    )
    return None


# Callback Купить на неделю
@dp.callback_query_handler(text="callback_buy2")
async def CallbackBuy2(callback_query: types.CallbackQuery) -> None:
    logger.info(
        "callback_buy2 from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await callback_query.bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=f"{text.buy_text}<code>{callback_query.id}:{text.buy2_cash}</code>",
        reply_markup=keyboard.Buy2LinkKeyboard()
    )
    return None


# Callback Купить на месяц
@dp.callback_query_handler(text="callback_buy3")
async def CallbackBuy3(callback_query: types.CallbackQuery) -> None:
    logger.info(
        "callback_buy3 from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await callback_query.bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=f"{text.buy_text}<code>{callback_query.id}:{text.buy3_cash}</code>",
        reply_markup=keyboard.Buy3LinkKeyboard()
    )
    return None


# Callback Купить наавсегда
@dp.callback_query_handler(text="callback_buy4")
async def CallbackBuy4(callback_query: types.CallbackQuery) -> None:
    logger.info(
        "callback_buy4 from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await callback_query.bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=f"{text.buy_text}<code>{callback_query.id}:{text.buy4_cash}</code>",
        reply_markup=keyboard.Buy4LinkKeyboard()
    )
    return None


@dp.callback_query_handler(text="callback_menu")
async def CallbackMenu(callback_query: types.CallbackQuery) -> None:
    logger.info(
        "callback_menu from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await callback_query.bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.main_text,
        reply_markup=keyboard.BuyKeyboard()
    )
    return None
