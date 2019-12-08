import telebot
import os
from flask import Flask
import requests

TOKEN = "1043775072:AAEp_iiUNllkKGaekaEFwOMGc9TKOoCRrcs"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
talker_url = "http://127.0.0.1:8000"


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
                 'Hello, ' + message.from_user.first_name + '\nБот отправляет Зефирному монстру все сообщения, написанные в чат')


@bot.message_handler(commands=['help'])
def start(message):
    bot.reply_to(message, ' Напиши сообщение, и его произнесет Зефирный монстр')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    # bot.reply_to(message, message.chat.id)
    if (message.chat.id == -287977201):
        if (message.text[0] == 'C'):
            requests.post(talker_url, data=str("У нас Крит! ").encode('utf-8'))
    else:
        requests.post(talker_url, data=str(message.text).encode('utf-8'))


bot.polling(timeout=26784000)

if __name__ == "__main__":
    server.run(host="127.0.0.1", port=int(os.environ.get('PORT', 5000)))
