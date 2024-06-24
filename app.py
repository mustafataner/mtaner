import os
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from telegram import Bot
from telegram.constants import ParseMode

# Duyuru sayfası URL'si
URL = 'http://www.diyarbakir.gov.tr/duyurular'

# Telegram bot token ve chat id ortam değişkenlerinden alınıyor
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = Bot(token=BOT_TOKEN)

async def send_telegram_message(image_path):
    with open(image_path, 'rb') as photo:
        await bot.send_photo(chat_id=CHAT_ID, photo=photo)

def capture_screenshot(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    driver.get(url)
    screenshot_path = "/tmp/duyurular_screenshot.png"
    driver.save_screenshot(screenshot_path)
    driver.quit()
    return screenshot_path

async def check_for_updates():
    screenshot_path = capture_screenshot(URL)
    if screenshot_path:
        await send_telegram_message(screenshot_path)
    
    while True:
        await asyncio.sleep(300)  # 5 dakika bekle
        new_screenshot_path = capture_screenshot(URL)
        if new_screenshot_path:
            await send_telegram_message(new_screenshot_path)

if __name__ == '__main__':
    asyncio.run(check_for_updates())
