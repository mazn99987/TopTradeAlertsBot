
import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = os.getenv("TG_TOKEN")
if not TOKEN:
    raise RuntimeError("Environment variable TG_TOKEN is missing. Set it in Render's dashboard.")

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(m: Message):
    await m.answer("هلا مازن! البوت شغال ✅\nاكتب /help لعرض الأوامر.")

@dp.message(Command("help"))
async def help_(m: Message):
    await m.answer(
        "الأوامر المتاحة:\n"
        "/start - تشغيل البوت\n"
        "/help - المساعدة\n"
        "/news - مثال خبر (نربط لاحقًا بمصادر السوق)"
    )

@dp.message(Command("news"))
async def news(m: Message):
    # TODO: أربط هنا مصادر الأخبار الحقيقية (RSS/APIs)
    await m.answer("📰 مثال خبر: السوق الأمريكي يتحرك اليوم — سنربط المصدر لاحقًا.")

@dp.message()
async def echo(m: Message):
    # رد افتراضي على أي رسالة نصية
    if m.text:
        await m.answer(f"وصلتني: {m.text}")
    else:
        await m.answer("📎 وصلتني رسالة غير نصية.")

async def main():
    # Start long-polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
