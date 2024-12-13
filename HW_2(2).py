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
