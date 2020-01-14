from requests_html import HTML
from requests import get

document = get('https://alternativlos.org/').content
html = HTML(html=document)

episodes = html.find('ul', first=True).find('li')
print(f'{len(episodes)} available episodes')
for episode in episodes:
    print(episode.text)
