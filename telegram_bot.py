import telegram
import requests
from bs4 import BeautifulSoup
import asyncio 

async def scrape_website():
    url = "https://www.moh.gov.et/site/articles-3-col" 
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url, {'timeout': 60})
    soup = BeautifulSoup(response.content, "html.parser")
    
    img_elements = soup.find_all("img", class_="image-style-large")
    img_urls = [element["src"] for element in img_elements]
    
    h5_elements = soup.find_all("h5", class_="field-content")
    h5_data = [element.text.strip() for element in h5_elements]
    
    p_elements = soup.find_all("p")
    p_data = [element.text.strip() for element in p_elements]
    
    return img_urls, h5_data, p_data

async def send_message_to_channel(bot, channel_id, message):
    await bot.send_message(chat_id=channel_id, text=message)

async def send_images_to_channel(bot, channel_id, image_urls):
    for url in image_urls:
        await bot.send_photo(chat_id=channel_id, photo=url)

async def main():
    while True:
        bot = telegram.Bot(token="6309059679:AAHJkh8_LHbhrDXiShZX-9wZNKDZ5mEdi1c")  
        channel_id = "@Moh_health"  
        
        img_urls, h5_data, p_data = await scrape_website()
        
        await send_images_to_channel(bot, channel_id, ["https://www.moh.gov.et/site/sites/default/files/styles/large/public/2023-05/344796862_633251454841378_281637696212224550_n.jpg?itok=MyFiItHE", "https://www.moh.gov.et/site/sites/default/files/styles/large/public/2023-05/photo_2023-05-29_21-58-53.jpg?itok=mdsjb6vn", "https://www.moh.gov.et/site/sites/default/files/styles/large/public/2023-05/11.jpg?itok=y_NYOpRE"])
        
        for data in h5_data:
            await send_message_to_channel(bot, channel_id, data)
        
        for data in p_data:
            await send_message_to_channel(bot, channel_id, data)
        
        await asyncio.sleep(3600) 

if __name__ == "__main__":
    asyncio.run(main())