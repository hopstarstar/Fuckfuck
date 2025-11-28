import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import os

TOKEN = os.getenv("8301751505:AAGMrreQgWuEhDpjA_dmYDP0viNueMJMVE4")
dp = Dispatcher()

codes = {
    "8567": "https://site.com/link1",
    "2345": "https://site.com/link2",
    "3333": "https://site.com/link3",
    "4444": "https://site.com/link4",
    "5555": "https://site.com/link5",
}

kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Написать код")]],
    resize_keyboard=True,
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Нажми кнопку чтобы ввести код.", reply_markup=kb)

@dp.message(lambda m: m.text=="Написать код")
async def ask(message: types.Message):
    await message.answer("Введите код:")

@dp.message()
async def check(message: types.Message):
    t = message.text.strip()
    if t in codes:
        await message.answer(f"Код верный!\n{codes[t]}")
    else:
        await message.answer("❌ Неверный код.")
    asyncio.create_task(clear(message))

async def clear(message: types.Message):
    await asyncio.sleep(1800)
    for i in range(100):
        try:
            await message.bot.delete_message(message.chat.id, message.message_id-i)
        except:
            pass

async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
