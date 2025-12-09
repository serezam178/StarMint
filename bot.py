from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio

TOKEN = "8434285555:AAE8yQZHATVVZH2aV5N88FFaHLMbBuHKjg8"

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def start_handler(message: types.Message):
        text = (
            "✨ Искал где купить Stars и NFT?\n"
            "⭐️ Хочешь по самой низкой цене и мгновенно?\n"
            "🎁 Telegram Premium, подарки, Stars — всё в одном боте!\n\n"
            "💎 Переходи и покупай прямо сейчас:\n"
            "👉 @StarMintAppBot"
        )
        await message.answer(text)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
