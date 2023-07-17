## Prerequisites

To run this code, you need to have the following dependencies installed:

- Python (version 3.7 or higher)
- `telegram` library (install via `pip install python-telegram-bot`)
- `requests` library (install via `pip install requests`)
- `beautifulsoup4` library (install via `pip install beautifulsoup4`)

You will also need to create a Telegram bot and obtain an API token. Follow the official documentation to create a new bot and obtain the token: [Creating a new bot](https://core.telegram.org/bots#6-botfather).

## Installation

1. Clone the repository or download the script file.

2. Install the required dependencies by running the following command in your terminal:

```shell
pip install -r requirements.txt
```

3. Replace the placeholder token and chat ID in the `main()` function with your own Telegram bot token and chat ID. You can find the chat ID by sending a message to the bot and then accessing the following URL in your browser: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`.

## Usage

To run the script, execute the following command in your terminal:

```shell
python main.py
```

The script will start scraping headlines from the BBC News website every 30 seconds and send them as messages to the specified Telegram chat using the provided bot token.

## How it works

The script consists of the following main components:

1. **Scraping the Website**: The `scrape_website()` function uses the `requests` library to send an HTTP GET request to the BBC News website and retrieve the HTML content. It then uses the `beautifulsoup4` library to parse the HTML and extract the headlines.

2. **Sending Messages to Bot**: The `send_message_to_bot()` function utilizes the `telegram` library to send messages to the specified chat ID using the provided bot token.

3. **Main Function**: The `main()` function is the entry point of the script. It creates an instance of the `telegram.Bot` class using the provided bot token. It then enters an infinite loop where it scrapes the website, iterates over the extracted headlines, and sends them as messages to the Telegram chat. The loop pauses for 3600 seconds between each iteration using `asyncio.sleep()`.

## Customization

Feel free to modify the code according to your requirements. Here are a few suggestions for customization:

- **Target Website**: You can change the `url` variable in the `scrape_website()` function to scrape headlines from a different website.

- **Scraping Logic**: If you want to extract different information from the website, you can modify the logic in the `scrape_website()` function accordingly. Refer to the `beautifulsoup4` documentation for more details on HTML parsing and navigation: [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

- **Scraping Frequency**: You can adjust the sleep duration in the `main()` function to control how often the script scrapes the website and sends messages to the Telegram chat. Keep in mind that excessive scraping can put a strain on the website's server and violate their terms of service.

## License

This code is provided under the [MIT License](LICENSE). Feel free to use and modify it according to your needs.

## Acknowledgements

- The code in this script is based on the examples provided in the official documentation of the libraries used:
  - [Telegram Bot API](https://core.telegram.org/bots/api)
  - [Requests Library](https://docs.python-requests.org/en/latest/)
  - [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

- Special thanks to the developers of the `telegram`, `requests`, and `beautifulsoup4` libraries for their excellent work in creating and maintaining these useful libraries.
