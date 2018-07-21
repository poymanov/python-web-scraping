import requests
from bs4 import BeautifulSoup

url = 'https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/';

request = requests.get(url)
content = request.content

data = BeautifulSoup(content, 'html.parser')

all = data.find_all('div', {'class': 'propertyRow'})

for item in all:
    price = item.find('h4').text.strip()
    print(price)
