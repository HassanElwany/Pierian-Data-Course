import requests
from bs4 import BeautifulSoup

authors = set()
quotes_list = []

result = requests.get("http://quotes.toscrape.com/")

source = result.text

# parse the source content
soup = BeautifulSoup(source, "lxml")
# print(soup)

authors_name = soup.select("small", class_='author')
# print(len(authors_name))
quotes = soup.select("div.quote span.text")
# print(len(quotes))
tag_items = soup.select("span.tag-item a.tag")
# print(len(tag_items))
for tag in tag_items:
    print(tag.text)

for i in range(len(quotes)):
    authors.add(authors_name[i].text)
    quotes_list.append(quotes[i].text)
print(authors)
print(quotes_list)
print('#'*100)
page = 1
the_authors = set()
while True:
     
    r = requests.get(f'http://quotes.toscrape.com/page/{page}/')
    source = r.text
    if 'No quotes found!' in r.text:
        break
    soup = BeautifulSoup(source, "lxml")
    authors_name = soup.select("small", class_='author')
    for i in range(len(authors_name)):
        the_authors.add(authors_name[i].text)
    page+= 1 
    

print(the_authors)
