import requests 
from bs4 import BeautifulSoup
import time


def get_price_of_quote(quote):
    site_name = 'https://www.google.com/search?q=cotacao+%s&rlz=1C1SQJL_pt-BRBR830BR830&oq=cotacao+vvar3&aqs=chrome..69i57j0l5.2183j1j7&sourceid=chrome&ie=UTF-8' % (quote)
    page = requests.get(site_name)
    bs = BeautifulSoup(page.content,features="lxml")
    tr = bs.findAll("tr")
    links = []
    for span in tr:
        links.extend(span.findAll('span'))
    price_of_quote =links[3].find(text=True)
    return price_of_quote

while True:
    try:
        quote = 'vvar3'
        print(get_price_of_quote(quote))
        time.sleep(1)
    except:
        time.sleep(3)