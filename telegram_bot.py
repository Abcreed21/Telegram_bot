import telegram
import requests
from bs4 import BeautifulSoup
import time
import asyncio

async def scrape_website():
    url = "https://www.moh.gov.et/site/articles-3-col?page=0"
    response = requests.get(url, timeout=30)
    soup = BeautifulSoup(response.content, "html.parser")
    headings = soup.find_all("p")
    return [heading.text.strip() for heading in headings]

async def send_message_to_channel(bot, channel_id, message):
    await bot.send_message(chat_id=channel_id, text=message)

async def main():
    bot = telegram.Bot(token="6309059679:AAHJkh8_LHbhrDXiShZX-9wZNKDZ5mEdi1c")
    channel_id = "@Moh_health"
    while True:
        data = await scrape_website()
        for item in data:
            await send_message_to_channel(bot, channel_id, item)
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())