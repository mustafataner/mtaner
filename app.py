import requests
from bs4 import BeautifulSoup
from telegram import Bot
from time import sleep

# Duyuru sayfası URL'si
URL = 'http://www.diyarbakir.gov.tr/duyurular'

# Telegram bot token ve chat id
BOT_TOKEN = '7330415458:AAHcjDsePpNm7LA8dfWf2qwCmNhCLG6wCdw'
CHAT_ID = '-4279731069'

bot = Bot(token=BOT_TOKEN)

def send_telegram_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

def get_latest_announcement(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # En son duyuruyu seçiyoruz (ilk <a> etiketi)
    latest_announcement = soup.find('a', href=True)
    if latest_announcement:
        return latest_announcement['href']
    return None

def check_for_updates():
    latest_announcement = get_latest_announcement(URL)
    if latest_announcement:
        send_telegram_message(f"Son duyuru: {latest_announcement}")
    else:
        send_telegram_message("Duyuru bulunamadı.")
    while True:
        sleep(900)  # 15 dakika bekle
        new_announcement = get_latest_announcement(URL)
        if new_announcement != latest_announcement:
            send_telegram_message(f"Yeni duyuru: {new_announcement}")
            latest_announcement = new_announcement

if __name__ == '__main__':
    check_for_updates()
