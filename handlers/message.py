# SO2 SCAM BOT BY github.com/Vlad2030

from aiogram import types
from loguru import logger

from keyboards import keyboard
from loader import dp
from modules import text


# /start
@dp.message_handler(commands="start")
async def start(message: types.Message) -> None:
    logger.info(
        "/start from {user_id} id",
        user_id=message.from_user.id
    )
    await message.answer(
        text.main_text,
        reply_markup=keyboard.BuyKeyboard()
    )
    return None
