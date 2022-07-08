from bs4 import BeautifulSoup
import requests as rq
import random as rd
from tkinter import *

######################## bs4, requests, url ########################
URL = "https://github.com/selcukemreozer/English-Playground/blob/main/kelime_bankalari/a1.txt"
try:
    page = rq.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll("td", {"id": "LC1"})

    results = str(results)

except rq.exceptions.ConnectionError:
    print("internet bağlantısı yok")



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


def secenekBelirleyici(kelimeBankasi):
    """
    Burası biraz kafa karışıklığına sebep olabiliyor. En azından benim kafam karıştı.
    O yüzden bu açıklamayı yazıyorum.
    :param kelimeBankasi: her kelimenin anlamıyla birlikte tek bir string eleman olduğu
    bir liste.

    Aşağıda 'secim_ = rd.choice(kelimeBankasi)' satırında split kullanmayıp aşağı
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
    ingilizceKelime, turkcesi = secim_.split(':')

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

########################       tkinter      ########################

def interface():

    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
    def paket(cevap_butonNo = 0):
        global oncekiDogruCevap
        global butonHafiza
        global oncekiKelime_ # global değişken olmalı çünkü oncekiKelime_ 'yi aklında tutuyor
        # global değişkene ihtiyaç duydum çünkü fonksiyonu tuşla çağırdığımız için
        # return değişkenleri saklamanın yolunu bulamadım

        try:
            if butonHafiza == cevap_butonNo:
                dogruYanlis.config(text = "doğru bildin!")

            else:
                dogruYanlis.config(text = oncekiDogruCevap)
        except NameError:
            dogruYanlis.config()
            butonHafiza = -1

        kelimeBankasi = RAKES_BankaDuzenleyici(results)
        secenekler = secenekBelirleyici(kelimeBankasi)
        dogruCevap = secenekler[1]
        secenek1 = secenekler[2].split(':')[1]
        secenek2 = secenekler[3].split(':')[1]

        try:
            if oncekiKelime_ == secenekler[0]:
                # print(f"tekrar:{oncekiKelime_}:{secenekler[0]}") >> KONTROL SİSTEMİ
                paket()
                # önceki kelime ile yeni kelime aynı ise özyineleme ile
                # tekrar yeni bir kelime çekiliyor
            else:
                soru.config(text=secenekler[0])
                # print(f"şimdi oldu:{oncekiKelime_}:{secenekler[0]}") >> KONTROL SİSTEMİ
                oncekiKelime_ = secenekler[0]
                oncekiDogruCevap = secenekler[0]+">>"+secenekler[1]

                butonNo = rd.randint(1, 3)

                if butonNo == 1:
                    butonHafiza = 1
                    buton1.config(text=dogruCevap)  # cevap(sorulan ingilizce kelimenin türkçesi)
                    buton2.config(text=secenek1)  # diger secenek 1'in türkçesi
                    buton3.config(text=secenek2)  # diger secenek 2'nin türkçesi

                elif butonNo == 2:
                    butonHafiza = 2
                    buton1.config(text=secenek1)  # diger secenek 1'in türkçesi
                    buton2.config(text=dogruCevap)  # cevap(sorulan ingilizce kelimenin türkçesi)
                    buton3.config(text=secenek2)  # diger secenek 2'nin türkçesi

                else:
                    butonHafiza = 3
                    buton1.config(text=secenek2)  # diger secenek 2'nin türkçesi
                    buton2.config(text=secenek1)  # diger secenek 1'in türkçesi
                    buton3.config(text=dogruCevap)  # cevap(sorulan ingilizce kelimenin türkçesi)

        except NameError:
            # global değişkene ilk seferde bir şey atayamazdım çünkü fonksiyon çağrıldığında
            # hep aynı atama gerçekleşecekti(örn. oncekiKelime_ = "") ve değişken görevini
            # yerine getiremeyecekti.
            oncekiKelime_ = ""
            paket()
            # oncekiKelime_ ilk değerini kazandıktan sonra özyinelme ile tekrar bir değer
            # ataması gerçekleşiyor

    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

    pencere = Tk()
    pencere.resizable(False, False)
    pencere.title('English-Playground')
    pencere.geometry('700x500+710+290')
    pencere.columnconfigure(0, weight=1)
    pencere.columnconfigure(1, weight=1)
    pencere.columnconfigure(2, weight=1)

    soru = Label(pencere, text = "", bg = "white", anchor = CENTER, font = ("Arial", 25))
    soru.grid(column = 1, row = 0, padx = 30, pady = 30)

    dogruYanlis = Label(pencere, text = "", font = ("Arial", 15))
    dogruYanlis.grid(column = 1, row = 2, padx = 10, pady = 10)

    buton1 = Button(pencere, text = "", height = 1, width = 11, font = ("Arial", 20), command = lambda: paket(1))
    buton2 = Button(pencere, text = "", height = 1, width = 11, font = ("Arial", 20), command = lambda: paket(2))
    buton3 = Button(pencere, text = "", height = 1, width = 11, font = ("Arial", 20), command = lambda: paket(3))

    buton1.grid(column = 0, row = 1)
    buton2.grid(column = 1, row = 1)
    buton3.grid(column = 2, row = 1)
    paket()
    mainloop()

interface()