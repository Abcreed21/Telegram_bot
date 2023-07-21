# Website Scraper and Telegram Publisher

This Python script allows you to scrape data from a website and publish it to a Telegram channel. You can use it to stay updated with the latest articles and images from the Ethiopian Ministry of Health website.

## Dependencies

Before you run the script, you'll need to install a few Python packages:

- [requests](https://docs.python-requests.org/en/latest/): Used to fetch the website's HTML content.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Used for parsing and navigating the HTML content.
- [Telegram Bot API](https://python-telegram-bot.readthedocs.io/en/stable/): Used for sending messages and images to the Telegram channel.
- [IPython](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html#introduction): Used for displaying images when running the script in an IPython environment.

You can install these packages by running the following command in your terminal:

```bash
pip install requests beautifulsoup4 python-telegram-bot ipython
```

## Setup

1. First, you'll need to get a Telegram bot token. If you don't have one, you can create a new bot on Telegram by talking to the [BotFather](https://core.telegram.org/bots#botfather). Copy the token, and paste it in the `token` variable in the code.

2. Next, specify the Telegram channel ID where you want to publish the scraped data. Replace `@Moh_health` with your channel's username or chat ID in the `channel_id` variable.

## How it Works

This script scrapes articles and images from the Ethiopian Ministry of Health website. It connects to the website, finds all the `<h5>` elements with the class "field-content" (assumed to be article headings), and extracts the text from them.

Then, it looks for all the `<a>` elements with the class "overlay-target-link" (assumed to be links to articles) and extracts their `href` attribute. If the link contains an `<img>` tag, the script will download and display the image and send it to the Telegram channel.

The process is repeated every hour to keep your Telegram channel up to date with the latest information from the Ministry of Health website.

## How to Run

To run the script, simply execute the Python file. For example:

```bash
python your_script_file.py
```

The script will start fetching data and sending it to your Telegram channel.

## Important Note

- The website's structure may change over time, which could lead to the script not working correctly. Please check and update the code accordingly if needed.

- Make sure to handle exceptions properly, as the script has built-in timeout handling when sending data to Telegram (`telegram.error.TimedOut`). It waits for 5 seconds and retries in case of a timeout.