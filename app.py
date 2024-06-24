import requests
from bs4 import BeautifulSoup
from telegram import Bot
from time import sleep

# Duyuru sayfası URL'si
URL = 'http://www.diyarbakir.gov.tr/duyurular'

# Telegram bot token ve chat id
BOT_TOKEN = 'your_telegram_bot_token'
CHAT_ID = 'your_chat_id'

bot = Bot(token=BOT_TOKEN)

def send_telegram_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

def get_page_content(url):
    response = requests.get(url)
    return response.text

def check_for_updates():
    initial_content = get_page_content(URL)
    while True:
        sleep(900)  # 15 dakika bekle
        new_content = get_page_content(URL)
        if new_content != initial_content:
            send_telegram_message('Diyarbakır Valiliği duyuru sayfasında yeni bir duyuru var.')
            initial_content = new_content

if __name__ == '__main__':
    check_for_updates()
