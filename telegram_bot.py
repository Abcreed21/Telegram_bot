import telegram
import requests
from bs4 import BeautifulSoup
import time
import asyncio

async def scrape_website():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    headings = soup.find_all("h3", class_="gs-c-promo-heading__title")
    return [heading.text.strip() for heading in headings]

async def send_message_to_bot(bot, chat_id, message):
    await bot.send_message(chat_id=chat_id, text=message)

async def main():
    bot = telegram.Bot(token="6309059679:AAHJkh8_LHbhrDXiShZX-9wZNKDZ5mEdi1c")
    chat_id = "1487965128"
    while True:
        data = await scrape_website()
        for item in data:
            await send_message_to_bot(bot, chat_id, item)
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())