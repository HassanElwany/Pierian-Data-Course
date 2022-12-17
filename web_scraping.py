import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

source = result.content

soup = BeautifulSoup(source, "lxml")

print(soup)