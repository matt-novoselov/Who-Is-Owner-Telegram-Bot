# Who Is Owner Sticker

Source code of Aiogram 3.x and Pyrogram based telegram bot that can get Telegram User ID of the creator of Sticker or Custom emoji.

![](https://github.com/matt-novoselov/Who-Is-Owner-Telegram-Bot/blob/905a6c0ca0ae9b9ab9104f7c36dcf30871c046ff/Thumbnail.png)

[![Telegram Bot](https://github.com/matt-novoselov/matt-novoselov/blob/4fddb3cb2c7e952d38b8b09037040af183556a77/Files/telegram_button.svg)](https://t.me/WhoIsOwnerBot)

## Requirements
- Python 3.8
- aiogram 3.12.0
- Pyrogram 2.0.93
- TgCrypto 1.2.5
- python-dotenv 1.0.1
- fastapi 0.112.1
- uvicorn 0.30.6


## Installation
1. Clone repository using the following URL: `https://github.com/matt-novoselov/Who-Is-Owner-Telegram-Bot.git`
2. Create Environment File:
   - Create a file named `.env` in the root directory of the source folder.
   - Use the provided `.env.example` file as a template.
3. Replace the placeholder values with your specific configuration:
   - TELEGRAM_TOKEN: Insert your Telegram Bot Token obtained from the [BotFather](https://t.me/botfather).
   - SESSION_STRING: Pyrogram authorized session as a serialized string.
   - WEBHOOK_DOMAIN: Public SSL domain that will be listening for webhooks request from Telegram.
4. Build and run `main.py`

<br>

## Credits
Distributed under the MIT license. See **LICENSE** for more information.

Developed with ❤️ by Matt Novoselov
