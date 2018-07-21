import requests
from bs4 import BeautifulSoup

url = 'https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/';

request = requests.get(url)
content = request.content

data = BeautifulSoup(content, 'html.parser')

all = data.find_all('div', {'class': 'propertyRow'})

for item in all:
    price = item.find('h4').text.strip()
    address_data = item.findAll('span', {'class': 'propAddressCollapse'})
    address1 = address_data[0].text.strip()
    address2 = address_data[1].text.strip()

    try:
        beds = item.find('span', {'class': 'infoBed'}).find('b').text.strip()
    except Exception:
        beds = None

    try:
        sq_ft = item.find('span', {'class': 'infoSqFt'}).find('b').text.strip()
    except Exception:
        sq_ft = None

    try:
        full_baths = item.find('span', {'class': 'infoValueFullBath'}).find('b').text.strip()
    except Exception:
        full_baths = None

    try:
        half_baths = item.find('span', {'class': 'infoValueHalfBath'}).find('b').text.strip()
    except Exception:
        half_baths = None

    print(price)
    print(address1)
    print(address2)
    print(beds)
    print(sq_ft)
    print(full_baths)
    print(half_baths)
    print()
