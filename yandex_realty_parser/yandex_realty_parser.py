import requests
import tqdm
from bs4 import BeautifulSoup


def parse(link: str,
          headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                   'Accept-Language': 'en-GB,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate, br'},
          start_page=1, end_page=100, fields=('link', 'address')):
    html = requests.get(link, headers=headers).text
    soup = BeautifulSoup(html)
    print(soup.body)

if __name__ == "__main__":
    parse('https://realty.ya.ru/moskva/snyat/kvartira/odnokomnatnaya/?priceMax=42500&priceMin=38500')
