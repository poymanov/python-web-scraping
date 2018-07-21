import requests
from bs4 import BeautifulSoup

url = 'https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/';

request = requests.get(url)
content = request.content

data = BeautifulSoup(content, 'html.parser')
