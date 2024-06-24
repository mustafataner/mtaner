import requests
from lxml import html
from telegram import Bot
from telegram.constants import ParseMode
import asyncio
import os

# Duyuru sayfası URL'si
URL = 'http://www.diyarbakir.gov.tr/duyurular'

# Telegram bot token ve chat id ortam değişkenlerinden alınıyor
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = Bot(token=BOT_TOKEN)

async def send_telegram_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.HTML)

def get_latest_announcement(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)
    latest_announcement = tree.xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[3]/div[1]/div/div/a/@href')
    if latest_announcement:
        return "http://www.diyarbakir.gov.tr" + latest_announcement[0]
    return None

async def check_for_updates():
    latest_announcement = get_latest_announcement(URL)
    if latest_announcement:
        await send_telegram_message(f"Son duyuru: {latest_announcement}")
    else:
        await send_telegram_message("Duyuru bulunamadı.")
    
    while True:
        await asyncio.sleep(900)  # 15 dakika bekle
        new_announcement = get_latest_announcement(URL)
        if new_announcement != latest_announcement:
            await send_telegram_message(f"Yeni duyuru: {new_announcement}")
            latest_announcement = new_announcement

if __name__ == '__main__':
    asyncio.run(check_for_updates())
