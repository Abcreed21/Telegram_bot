import telegram
import requests
from bs4 import BeautifulSoup
import asyncio
from IPython.display import Image, display

async def scrape_website(bot, channel_id):
    url = "https://www.moh.gov.et/site/articles-3-col"
    response = requests.get(url, timeout=120)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the <h5> elements with class "field-content"
    headings = soup.find_all("h5", class_="field-content")

    # Find all the <a> elements with class "overlay-target-link"
    links_with_class = soup.find_all("a", class_="overlay-target-link")

    for link in links_with_class:
        # Print the href attribute of each link
        print("Found link with class 'overlay-target-link':", link['href'])

        # Check if the link has an <img> tag inside it
        if link.find("img"):
            image_url = link.img['src']
            print("Image URL:", image_url)

            # Display the image
            display(Image(url=image_url))

            # Download the image file
            image_file = requests.get(image_url)

            # Send the image to the channel
            await send_photo_to_channel(bot, channel_id, image_file.content)

    return [heading.text.strip() for heading in headings]


async def send_message_to_channel(bot, channel_id, message):
    try:
        await bot.send_message(chat_id=channel_id, text=message)
    except telegram.error.TimedOut:
        await asyncio.sleep(5)  # Wait for 5 seconds
        await send_message_to_channel(bot, channel_id, message)


async def send_photo_to_channel(bot, channel_id, image_content):
    try:
        # Create a file-like object from the image content
        image_file = telegram.InputFile(image_content)

        # Send the image to the channel
        await bot.send_photo(chat_id=channel_id, photo=image_file)
    except telegram.error.TimedOut:
        await asyncio.sleep(5)  # Wait for 5 seconds
        await send_photo_to_channel(bot, channel_id, image_content)


async def main():
    bot = telegram.Bot(token="6309059679:AAHJkh8_LHbhrDXiShZX-9wZNKDZ5mEdi1c")
    channel_id = "@Moh_health"

    while True:
        data = await scrape_website(bot, channel_id)
        for item in data:
            await send_message_to_channel(bot, channel_id, item)
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
