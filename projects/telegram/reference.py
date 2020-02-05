"""
Telegram bot the canteens of the TU Dresden.

It parses the website of the "Studentenwerk" to retrieve all canteens
and the dishes they serve today.

Please note that some vocabulary is based on the structure of this website.
There, the single canteens are presented as cards and variables containing
such an HTML element carry the "card" suffix.
"""
from typing import List, Dict, Any

import requests
from requests_html import HTML
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

TOKEN = '1097500800:AAHtnKhqPQUqmXA11-H2iRzTTQimQYW4PFY'
URL = 'https://www.studentenwerk-dresden.de/mensen/speiseplan/?view=list'


def all_canteens() -> Dict[str, Any]:
    """ Returns all canteens of the TU Dresden """
    print('Fetch all canteens')
    html = requests.get(URL).content
    site = HTML(html=html)
    cards = site.find('.card')

    found = {}
    for card in cards:
        headers = card.find('h3.card-header')
        if not headers:
            continue

        header = headers[0].text
        found[header] = card

    return found


def get_canteen_names() -> List[str]:
    """ List the names of all canteens at the TU Dresden. """
    return list(all_canteens().keys())


def dishes_for_canteen_card(canteen_card):
    """ Extracts the dishes from a given canteen card. """
    menu_items = canteen_card.find('li.swdd-link-list-item')
    dishes = list()

    for index, menu_item in enumerate(menu_items):
        dish_name = menu_item.find('span')[1].text
        dish_price = menu_item.find('strong')[0].text

        dish_price = dish_price.split('/')[0].strip().replace(' ', '')

        dishes.append({
            'name': dish_name,
            'price': dish_price
        })

    return dishes


def list_canteens(update, context):
    """
    Provides the user with a clickable list of all canteens
    at the TU Dresden.
    """
    print('hello')
    names = get_canteen_names()
    keyboard = [
        [InlineKeyboardButton(name, callback_data=name)]
        for name in names
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('🤔 Choose a canteen ⬇',
                              reply_markup=reply_markup)


def dishes_for_canteen(update, context):
    """
    Sends the current dishes for the selected canteen back to
    the user.
    """
    query = update.callback_query
    canteen_name = query.data
    canteen_card = all_canteens()[canteen_name]

    query.edit_message_text(text=f'Dishes for {canteen_name}')

    dishes = dishes_for_canteen_card(canteen_card)
    for dish in dishes:
        query.message.reply_text(f"{dish['name']} {dish['price']}")


def start_callback(update, context):
    update.message.reply_text("Welcome to my awesome bot!")


def start_bot():
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('list', list_canteens))
    updater.dispatcher.add_handler(CallbackQueryHandler(dishes_for_canteen))
    updater.dispatcher.add_handler(CommandHandler("start", start_callback))

    updater.start_polling()
    updater.idle()


start_bot()
