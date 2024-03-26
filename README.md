# Telegram Crypto and Forex Bot

## Overview:
This Telegram bot provides real-time information about the current prices of the top 5 cryptocurrencies and selected forex pairs. It integrates with Telegram to deliver this information promptly to users.

## Installation:
1. Clone the repository.
2. Ensure you have Python installed (preferably Python 3).
3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Setup:
1. Obtain Telegram API Token:
   - You need to obtain a Telegram Bot API token. You can do this by creating a new bot using [BotFather](https://core.telegram.org/bots#botfather) on Telegram.
   - After creating the bot, BotFather will provide you with a token. Copy this token for later use.

2. Set Up Django Environment Variables:
   - Create a `credentials.py` file in the project directory.
   - Add the following content to `credentials.py`, replacing `YOUR_BOT_TOKEN_HERE` with the token obtained from BotFather:
     ```python
     BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
     APP_NAME = 'codlearnprojectbot'
     ```

## Usage:
1. Run the Django server:
   ```bash
   python manage.py runserver
   ```

2. Interact with the bot on Telegram:
   - Start the bot by sending `/start` command.
   - Choose between cryptocurrency or forex information.
   - For cryptocurrency information, send the `/crypto` command.
   - For forex information, send the `/forex` command.

## Structure:
- `credentials.py`: Contains bot credentials. Make sure to replace placeholders with actual values.
- `bot.py`: Defines the Telegram bot class and its functionalities.
- `models.py`: Contains Django models for Telegram users, chats, and states.
- `processors.py`: Contains message processing functions for the bot.
- `urls.py`: Defines URL patterns for webhook handling and polling updates.
- `views.py`: Contains view functions for handling bot requests.

## Dependencies:
- Django: Web framework for building the backend.
- python-telegram-bot: Python wrapper for the Telegram Bot API.
- requests: HTTP library for making API requests.

## Contributors:
- Nima Ahmadi
- Nima87760@gmail.com





