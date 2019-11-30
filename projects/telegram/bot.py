import os
from datetime import date

import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler


TOKEN = os.getenv('BOT_TOKEN')
# TOKEN = ''


def get_lunch(day: int) -> list:
    """
    Fetch available dishes online.
    """
    url = 'https://www.studentenwerk-dresden.de/mensen/speiseplan/w0-d{}.html?view=list'.format(day)
    print('Fetching lunch from: {}'.format(url))

    content_raw = requests.get(url).content
    content = BeautifulSoup(content_raw, 'html.parser')

    alte_mensa_card = content.select('.card')[5]
    menu_items = alte_mensa_card.select('a.text-dark')

    dishes = list()
    for index, menu_item in enumerate(menu_items):

        dish_name = menu_item.select('span')[1].text
        dish_price = menu_item.select('strong')[0].text
        print('Dish {}'.format(index))
        print('- {}'.format(dish_name))
        if dish_price:
            dish_price = dish_price.split('/')[0].strip().replace(' ', '')
            print('=> {}'.format(dish_price))

        dishes.append({
            'name': dish_name,
            'price': dish_price
        })

    return dishes


def lunch_action(update, context):
    """
    Send back available dishes to the user.
    """
    print('Get lunch dishes')

    today = date.today()
    current_weekday = (today.weekday() + 1) % 6
    print('Current weekday is {}'.format(current_weekday))

    dishes = get_lunch(current_weekday)

    if not dishes:
        update.message.reply_text('No lunch today')
        return

    update.message.reply_text('Lunch on {}'.format(today.strftime('%d.%m.%y')))
    for dish in dishes:
        update.message.reply_text('{} {}'.format(dish['name'], dish['price']))


def start_bot():
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('lunch', lunch_action))

    updater.start_polling()
    updater.idle()


start_bot()

