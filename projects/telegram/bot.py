from requests import get
from requests_html import HTML
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

URL = 'https://www.studentenwerk-dresden.de/mensen/speiseplan/?view=list'
TOKEN = 'my_telegram_token'

updater = Updater(TOKEN, use_context=True)


def get_all_canteens():
    document = get(URL).content
    html = HTML(html=document)

    all_cards = html.find('.card')

    all_canteens = {}
    for card in all_cards:

        name_element = card.find('.card-header', first=True)
        if name_element is None:
            continue
        name = name_element.text

        all_dishes = []
        for dish in card.find('.swdd-link-list-item'):
            dish_name = dish.find('.align-items-center', first=True).text
            dish_price = dish.find('strong', first=True).text
            dish_dict = {
                'name': dish_name,
                'price': dish_price,
            }
            all_dishes.append(dish_dict)

        all_canteens[name] = all_dishes

    return all_canteens


def dishes_hanlder(update, context):
    canteens = get_all_canteens()
    dishes_for_alte_mensa = canteens['Alte Mensa in Dresden']

    for dish in dishes_for_alte_mensa:
        price = dish['price']

        if price == 'ausverkauft':
            continue

        student_price = price.split('/')
        student_price = student_price[0].strip()
        update.message.reply_text(f"🍕  {dish['name']}\n💰  {student_price}")


updater.dispatcher.add_handler(CommandHandler('dishes', dishes_hanlder))

updater.start_polling()
updater.idle()
