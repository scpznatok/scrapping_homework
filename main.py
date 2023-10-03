import requests
from bs4 import BeautifulSoup



url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url) 
soup = BeautifulSoup(response.text,"lxml")
name = soup.find_all('h4')
price = soup.find_all('h5')
some_data = dict()
for i in range(len(name)):
    print(name[i].text)
    print(price[i].text)
    print("______________")