from bs4 import BeautifulSoup
import urllib.request
import re

leslie_quotes = []
for i in range(48):
    print(i)
    url = "https://www.tvfanatic.com/quotes/characters/leslie-knope/page-%s.html," % str(i+1)
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')

    quote_div = soup.find('div', {'id': 'infinite'})
    quotes = quote_div.find_all('p')

    for quote in quotes:
        if len(quote.find_all('br')) > 0:
            just_leslie = re.findall('Leslie:[^<]*', str(quote))
            for line in just_leslie:
                line = line[8:]
                leslie_quotes.append(line)
        else:
            quote = quote.get_text()
            leslie_quotes.append(quote)

print(leslie_quotes)
