from requests_html import HTML
from requests import get

document = get('http://localhost:5000/people').content
html = HTML(html=document)

for person in html.find('.person'):
    text = person.text.split(',')
    name = text[0]
    age = int(text[1])
    print(name, age)
