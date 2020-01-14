from requests_html import HTML
from requests import get

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
