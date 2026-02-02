import asyncio
import random
from telethon import TelegramClient, events, errors
import config
from utils import logger, contains_keyword, clean_message

client = TelegramClient(config.SESSION_NAME, config.API_ID, config.API_HASH)

@client.on(events.NewMessage(chats=config.SOURCE_CHANNELS))
async def new_message_handler(event):
    raw_text = event.message.text
    
    if not raw_text:
        return

    if contains_keyword(raw_text, config.KEYWORDS):
        try:
            final_text = clean_message(raw_text)
            
            chat = await event.get_chat()
            chat_title = chat.title if chat.title else "Unknown Channel"

            logger.info(f"کلمه کلیدی در کانال '{chat_title}' پیدا شد.")

            delay = random.randint(config.MIN_DELAY, config.MAX_DELAY)
            logger.info(f" صبر به مدت {delay} ثانیه...")
            await asyncio.sleep(delay)

           
            source_link = f"\n\n🔗 منبع: {chat_title}"
            await client.send_message('me', final_text + source_link)
            
            logger.info(" پیام با موفقیت ذخیره شد.")

        except errors.FloodWaitError as e:
            logger.warning(f" محدودیت تلگرام! خوابیدن برای {e.seconds} ثانیه.")
            await asyncio.sleep(e.seconds)
            
        except Exception as e:
            logger.error(f" خطای پیش‌بینی نشده: {e}")

async def main():
    logger.info("🚀 ربات در حال راه‌اندازی است...")
    await client.start()
    logger.info(" ربات آنلاین شد و در حال شنود کانال‌هاست.")
    await client.run_until_disconnected()

if __name__ == '__main__':
    try:
        client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        logger.info(" ربات توسط کاربر متوقف شد.")