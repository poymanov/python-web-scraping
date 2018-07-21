import requests
from bs4 import BeautifulSoup
import pandas

base_url = 'https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/';
objects = []

request = requests.get(base_url)
content = request.content

data = BeautifulSoup(content, 'html.parser')

page_numbers = data.find('span', {'class': 'PageNumbers'}).findChildren()
page_numbers = len(page_numbers) * 10

for page in range(0, page_numbers, 10):
    url = "%st=0&s=%s.html" % (base_url, page)

    request = requests.get(url)
    content = request.content

    data = BeautifulSoup(content, 'html.parser')

    all = data.find_all('div', {'class': 'propertyRow'})

    for item in all:
        price = item.find('h4').text.strip()
        address_data = item.findAll('span', {'class': 'propAddressCollapse'})
        address = address_data[0].text.strip()

        try:
            location = address_data[1].text.strip()
        except Exception as e:
            location = None

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

        try:
            features = item.find('div', {'class': 'propertyFeatures'}).findAll('div', {'class': 'columnGroup'})

            lot_size = None

            for item in features:
                childs = item.findChildren()

                if len(childs) == 0: continue

                if 'Lot Size' in childs[0].text:
                    lot_size = childs[1].text.strip()

        except Exception as e:
            lot_size = None

        objects.append({
            'Price': price,
            'Address': address,
            'Location': location,
            'Beds': beds,
            'Sq. Ft': sq_ft,
            'Full Baths': full_baths,
            'Half Baths': half_baths,
            'Lot Size': lot_size
        })

df = pandas.DataFrame(objects)
df.to_csv('objects.csv')
