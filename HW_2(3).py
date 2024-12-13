import requests
import re

response = requests.get("http://quotes.toscrape.com/")
html = response.text

quotes = re.findall(r'<span class="text" itemprop="text">“(.*?)”</span>', html)

authors = re.findall(r'<small class="author" itemprop="author">(.*?)</small>', html)

for quote, author in zip(quotes, authors):
    print(f'"{quote}" - {author}')

links = re.findall(r'<a href="(.*?)"', html)

for link in links:
    print(link)
response = requests.get("http://books.toscrape.com/")
html = response.text

book_titles = re.findall(r'<h3><a href=".*?" title="(.*?)">', html)

book_prices = re.findall(r'<p class="price_color">£(.*?)</p>', html)

for title, price in zip(book_titles, book_prices):
    print(f'"{title}" - £{price}')
