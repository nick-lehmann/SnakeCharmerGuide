from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from time import time


updater = Updater(
    '1020549379:AAFbFYdKuZa4vLWUrhF7N8VySUV5Hj3gonE', use_context=True)


def censorship(update, context):
    blocked_words = ['java', 'sap']
    text = update.message.text

    for word in blocked_words:
        text = text.replace(word, '*' * len(word))

    update.message.reply_text(text)


def send_pic(update, context):
    name = update.message.text
    name = name[5:]
    url = f'https://source.unsplash.com/featured/?{name}&{time()}'
    print(url)
    update.message.reply_photo(url)


def hello(update, context):
    update.message.reply_text('Hello')


def ping_handler(update, context):
    update.message.reply_text('Pong 🏓')


def big_function(update, context):
    text = update.message.text
    text = text.replace('/big ', '')
    update.message.reply_text(text.upper())


updater.dispatcher.add_handler(MessageHandler(Filters.text, censorship))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('ping', ping_handler))
updater.dispatcher.add_handler(CommandHandler('big', big_function))
updater.dispatcher.add_handler(CommandHandler('pic', send_pic))

print('Started 🚀')
updater.start_polling()
updater.idle()
