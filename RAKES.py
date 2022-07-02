from bs4 import BeautifulSoup
import requests as rq
import random as rd

URL = "https://github.com/selcukemreozer/English-Playground/blob/main/kelime_bankalari/a1.txt"
page = rq.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll("td", {"id":"LC1"})

results = str(results)

for each in range(len(results)): # gereksiz html parçalarını ayıklıyor ve sadece kelimeler kalıyor.
    # (Bilmiyorum sanki daha mantıklı ve kullanışlı bir yolu varmış gibi geliyor.)

    if results[each] == ">":
        sonuc = results[each:]

        for each2 in range(len(results[each:])):

            if results[each2+each] == "<":
                kelimeler = results[each+1:each2+each]
                break
        break

print(kelimeler)

list_ = kelimeler.split(",") # burada kelimeler ve karşılıkları gruplara ayrılıyor ve listede tutuluyor.
                             # Ör.["apple:elma", "car:araba"]
secim = rd.choice(list_)     # rastgele bir kelime veanlamı seçiliyor

cevap = input(secim.split(":")[0]+">") # seçilen kelime gösterilip anlamı soruluyor

if cevap == secim.split(":")[1]:
    print("doğru")
