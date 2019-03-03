import requests 
from bs4 import BeautifulSoup
import time

quote = 'vvar3'

def get_price_of_quote(quote):
    site_name = 'http://www.fundamentus.com.br/detalhes.php?papel=' + quote
    page = requests.get(site_name)
    bs = BeautifulSoup(page.content,features="lxml")
    span = bs.findAll("span", {"class": "txt"})
    price_of_quote =span[3].find(text=True)
    return price_of_quote

while True:
    print(get_price_of_quote(quote))
    time.sleep(1)