#import libraries
import pandas as pd
import telegram

#fetch telegram api credentials
telebot_credentials = pd.read_csv('telegram_bot_credentials.csv').iloc[0]

#fetch chat id, token from the csv just fetched
my_chat_id, my_token = telebot_credentials['chat_id'], telebot_credentials['my_token']

#initialize token
bot = telegram.Bot(token=my_token)

