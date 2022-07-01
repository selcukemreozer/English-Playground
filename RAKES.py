from bs4 import BeautifulSoup
import requests as rq

URL = "https://github.com/selcukemreozer/English-Playground/blob/main/kelime_bankalari/a1.txt"
page = rq.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll("td", {"id":"LC1"})
print(results)
list_ = list()

