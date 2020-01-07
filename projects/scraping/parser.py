from requests_html import HTML
from requests import get


def parse_local():
    document = get('http://localhost:5000/people').content
    html = HTML(html=document)

    for person in html.find('.person'):
        text = person.text.split(',')
        name = text[0]
        age = int(text[1])
        print(name, age)


def parse_alternativlos():
    document = get('https://alternativlos.org/').content
    html = HTML(html=document)

    episodes = html.find('ul', first=True).find('li')
    print(len(episodes))


def parse_tu_dresden():
    document = get('https://tu-dresden.de/').content
    html = HTML(html=document)

    titles = html.find('.owl-carousel', first=True).find('.teaser-bottom')
    print([title.text for title in titles])


def parse_spotify_charts():
    document = get(
        'https://spotifycharts.com/regional/global/weekly/latest').content
    html = HTML(html=document)

    table = html.find('.chart-table tbody', first=True)
    songs = table.find('tr')

    for song in songs[:10]:
        print(
            song.find('.chart-table-position', first=True).text,
            song.find('.chart-table-track', first=True).text,
        )
