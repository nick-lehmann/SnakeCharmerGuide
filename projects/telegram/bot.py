from requests import get
from requests_html import HTML

URL = 'https://www.studentenwerk-dresden.de/mensen/speiseplan/?view=list'
TOKEN = '713760546:AAFCvsHVC-HiFZ2wQAaFbHwwHFbvyPQIf-E'


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


canteens = get_all_canteens()
dishes_for_mensa_johanstadt = canteens['Mensa Johannstadt in Dresden']

for dish in dishes_for_mensa_johanstadt:
    print(f"🍕  {dish['name']} 💰  {dish['price']}")
