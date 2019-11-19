from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = '921290224:AAHQhv4n2GsKPdJf9xRricDan_uyPUeE6lc'


def hello(update, context):
    update.message.reply_text('pong')


def msg(update, context):
    print('Hello')
    print(update.message)


updater = Updater(TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('ping', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.all, msg))

updater.start_polling()
updater.idle()
