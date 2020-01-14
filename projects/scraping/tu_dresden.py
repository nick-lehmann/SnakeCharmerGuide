from requests_html import HTML
from requests import get

document = get('https://tu-dresden.de/').content
html = HTML(html=document)

titles = html.find('.owl-carousel', first=True).find('.teaser-bottom')
print([title.text for title in titles])
