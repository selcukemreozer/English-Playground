from bs4 import BeautifulSoup
import requests as rq
import random as rd
from tkinter import *

######################## bs4, requests, url ########################
URL = "https://github.com/selcukemreozer/English-Playground/blob/main/kelime_bankalari/a1.txt"
page = rq.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll("td", {"id": "LC1"})

results = str(results)

####################################################################
def RAKES_BankaDuzenleyici(results_):
    for each in range(len(results_)):  # gereksiz html parçalarını ayıklıyor ve sadece kelimeler kalıyor.
        # (Bilmiyorum sanki daha mantıklı ve kullanışlı bir yolu varmış gibi geliyor.)

        if results_[each] == ">":
            for each2 in range(len(results_[each:])):

                if results_[each2 + each] == "<":
                    tum_kelimeler = results_[each + 1:each2 + each]  # tüm ing ve tr kelimeler str halinde tek parça
                    kelimeListesi = tum_kelimeler.split(',')  # her kelimenin ing ve trsi bir eleman olacak şekilde  listeleme
                    break
            break

    return  kelimeListesi


def secenek_Belirleyici(kelimeBankasi):
    """
    Burası biraz kafa karışıklığına sebep olabiliyor. En azından benim kafam karıştı.
    O yüzden bu açıklamayı yazıyorum.
    :param kelimeBankasi: her kelimenin anlamıyla birlikte tek bir string eleman olduğu
    bir liste.

    Aşağıda 'secim_ = rd.choice(kelimeBankasi)' satırında split kullanmayıp aşağı iki
    satırda kullanma sebebim
    secim_ = 'kelime:turkcesi'
    şeklinde kalmalı çünkü 'while'döngüsünde karşılaştırmaya giriyor.
    Karşılaştırma düzgün çalışmalı.

    örn:
    secim_ = rd.choice(kelimeBankasi).split(':') olsaydı >> secim_ = ['red','kırmızı']
    olacaktı. Ve

    digerSecenek1 = 'kırmızı:red'
    olsaydı >> if digerSecenek1 == secim_:

    bunu fark etmeyecekti çünkü:

    if 'kırmızı:red' == ['red','kırmızı'] >> False döndürecekti.

    Ve random fonksiyonu aynı değeri dödürene kadar bu hata fark edilemeyecekti.
    :return:
    """
    secim_ = rd.choice(kelimeBankasi)
    ingilizceKelime = secim_.split(':')[0]
    turkcesi = secim_.split(':')[1]

    digerSecenek1 = rd.choice(kelimeBankasi)
    digerSecenek2 = rd.choice(kelimeBankasi)

    while True:
        if digerSecenek1 == secim_:
            digerSecenek1 = rd.choice(kelimeBankasi)
            continue

        elif digerSecenek1 == digerSecenek2:
            digerSecenek2 = rd.choice(kelimeBankasi)
            continue

        elif digerSecenek2 == secim_:
            digerSecenek2 = rd.choice(kelimeBankasi)
            continue

        else:
            break

    return [ingilizceKelime, turkcesi, digerSecenek1, digerSecenek2]



"""
print(kelimeBankasi[0])
print(kelimeBankasi[1])
# Ör.["apple:elma", "car:araba"]
secim = rd.choice(kelimeBankasi[1])  # rastgele bir kelime veanlamı seçiliyor

cevap = input(secim.split(":")[0] + ">")  # seçilen kelime gösterilip anlamı soruluyor

if cevap == secim.split(":")[1]:
    print("doğru")
"""

########################       tkinter      ########################
def interface():
    pencere = Tk()
    pencere.resizable(False, False)
    pencere.title('English-Playground')
    pencere.geometry('500x500+710+290')
    pencere.columnconfigure(0, weight=2)
    pencere.columnconfigure(1, weight=2)
    pencere.columnconfigure(2, weight=2)

    kelimeBankasi = RAKES_BankaDuzenleyici(results)
    secenekler = secenek_Belirleyici(kelimeBankasi)
    print(kelimeBankasi)
    print(secenekler)
    mainloop()

interface()