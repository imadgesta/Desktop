import sys

import  asyncio
from aiogram import Bot, Dispatcher, types

# -----------------------------------------
bot = Bot(token="6414955107:AAHVcAjsQEzrTei-RUU75vjtdsh3XLEJfY0")
# ---------------------------------------------------------------
dp = Dispatcher()






async def main():
    await dp.start_polling(bot)

 asyncio.run(main())