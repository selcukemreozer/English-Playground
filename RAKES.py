from bs4 import BeautifulSoup
import requests as rq
import re

URL = "https://github.com/selcukemreozer/English-Playground/blob/main/README.md"
page = rq.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll("div", {"id":"readme"})
results = str(results)
print(results)
list_ = list()

