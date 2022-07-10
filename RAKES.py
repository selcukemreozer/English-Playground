#$$ en son configKontrolcu inşa ediyordun. >> paket() çağırdığında defalarca aynı hatayı vermesin diye
#$$ aşağıda hata değişkenine ilk atamayı yapmak için paket() çağrılıyor o sırada defalarca hata alıyor
from bs4 import BeautifulSoup
import requests as rq
import random as rd
from tkinter import *
from tkinter import messagebox


def RAKES_bankaDuzenleyici(tip, kelime_bankasi_ismi):

    ######################## bs4, requests, url ########################
    global hata # program herhangi bir hata ile karşılaştığında gerekli yerlerin çalışmasını durdurucak

    try:
        hata = True

        if tip == "hazir":
            URL = "https://github.com/selcukemreozer/English-Playground/blob/main/kelime_bankalari/" + kelime_bankasi_ismi+".txt"
            page = rq.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.findAll("td", {"id": "LC1"})

            results = str(results)

            for each in range(len(results)):  # gereksiz html parçalarını ayıklıyor ve sadece kelimeler kalıyor.
                # (Bilmiyorum sanki daha mantıklı ve kullanışlı bir yolu varmış gibi geliyor.)

                if results[each] == ">":
                    for each2 in range(len(results[each:])):

                        if results[each2 + each] == "<":
                            tum_kelimeler = results[each + 1:each2 + each]  # tüm ing ve tr kelimeler str halinde tek parça
                            # her kelimenin ing ve trsi bir eleman olacak şekilde  listeleme
                            break
                    break


        elif tip=="topluluk":
            results = open("kelime_bankalari/"+kelime_bankasi_ismi+".txt", "r+", encoding="utf-8")
            tum_kelimeler = results.read()



        else:
            pass

        kelimeListesi = tum_kelimeler.split(',')
        return kelimeListesi

    except FileNotFoundError:
        messagebox.showwarning(title="HATA!", message="Aradığınız dosya bulunamadı!")
        hata = False

    except rq.exceptions.ConnectionError:
        messagebox.showerror(title="Bağlantı Hatası!", message="İnternet baplantısı sağlanamadı!")
        hata = False
    ####################################################################

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
####################################################################

########################       tkinter      ########################
def bankaSecimPenceresi():
    global hata

    bankaSecimPenceresi = Tk()
    bankaSecimPenceresi.resizable(False, False)
    bankaSecimPenceresi.title('RAKES')
    bankaSecimPenceresi.geometry('700x500+710+290')
    bankaSecimPenceresi.columnconfigure(0, weight=1)
    bankaSecimPenceresi.columnconfigure(1, weight=1)
    bankaSecimPenceresi.columnconfigure(2, weight=2)

    a1Buton = Button(bankaSecimPenceresi, text="a1", font=("Arial", 20),
                     command=lambda: [bisi("topluluk", "a1"), bankaSecimPenceresi.destroy()])

    a2Buton = Button(bankaSecimPenceresi, text="a2", font=("Arial", 20),
                     command=lambda: [bisi("topluluk", "a2"), bankaSecimPenceresi.destroy()])

    b1Buton = Button(bankaSecimPenceresi, text="b1", font=("Arial", 20),
                     command=lambda: [bisi("topluluk", "b1"), bankaSecimPenceresi.destroy()])

    b2Buton = Button(bankaSecimPenceresi, text="b2", font=("Arial", 20),
                     command=lambda: [bisi("topluluk", "b2"), bankaSecimPenceresi.destroy()])

    c1Buton = Button(bankaSecimPenceresi, text="c1", font=("Arial", 20),
                     command=lambda: [bisi("topluluk", "c1"), bankaSecimPenceresi.destroy()])

    c2Buton = Button(bankaSecimPenceresi, text="c2", font=("Arial", 20),
                     command=lambda: [bisi("topluluk", "c2"), bankaSecimPenceresi.destroy()])

    a1Buton.grid(column=0, row=0, sticky=E, padx=5, pady=50)
    a2Buton.grid(column=1, row=0, sticky=W, padx=5, pady=50)
    b1Buton.grid(column=0, row=1, sticky=E, padx=5, pady=5)
    b2Buton.grid(column=1, row=1, sticky=W, padx=5, pady=5)
    c1Buton.grid(column=0, row=2, sticky=E, padx=5, pady=50)
    c2Buton.grid(column=1, row=2, sticky=W, padx=5, pady=50)

def soruPenceresi(tip, kelimeBankasi_ismi):
    global hata
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
    def paket(cevap_butonNo = 0, configKontrolcu = True): # kısım1'de paket alacak bir cevap_butonNo değerine sahip değildir
                                  # o yüzden cevap_butonNo = 0
        global oncekiDogruCevap
        global butonHafiza
        global oncekiKelime_  # global değişken olmalı çünkü oncekiKelime_ 'yi aklında tutuyor
        # global değişkene ihtiyaç duydum çünkü fonksiyonu tuşla çağırdığımız için
        # return değişkenleri saklamanın yolunu bulamadım


        # if hata:


        try:
            kelimeBankasi = RAKES_bankaDuzenleyici(tip, kelimeBankasi_ismi)
            secenekler = secenekBelirleyici(kelimeBankasi)
            if butonHafiza == cevap_butonNo and configKontrolcu:
                dogruYanlis.config(text = "doğru bildin!")
            elif configKontrolcu:
                dogruYanlis.config(text = oncekiDogruCevap)
            else:
                pass

        except NameError:
            butonHafiza = -1

        dogruCevap = secenekler[1]
        secenek1 = secenekler[2].split(':')[1]
        secenek2 = secenekler[3].split(':')[1]

        try:
            if oncekiKelime_ == secenekler[0]: # kısım1
                # önceki kelime ile yeni kelime aynı ise özyineleme ile
                # tekrar yeni bir kelime çekiliyor
                # print(f"tekrar:{oncekiKelime_}:{secenekler[0]}") >> KONTROL SİSTEMİ
                paket()

            else:
                soru.config(text = secenekler[0])
                # print(f"şimdi oldu:{oncekiKelime_}:{secenekler[0]}") >> KONTROL SİSTEMİ
                oncekiKelime_ = secenekler[0]
                oncekiDogruCevap = secenekler[0]+" >> "+secenekler[1]

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

        #else:
            #pass
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
    if hata:
        # print("hata:",hata)
        soruPenceresi = Tk()
        soruPenceresi.resizable(False, False)
        soruPenceresi.title('RAKES')
        soruPenceresi.geometry('700x500+710+290')
        soruPenceresi.columnconfigure(0, weight=1)
        soruPenceresi.columnconfigure(1, weight=1)
        soruPenceresi.columnconfigure(2, weight=1)

        soru = Label(soruPenceresi, text = "", bg = "white", anchor = CENTER, font = ("Arial", 25))
        soru.grid(column = 1, row = 0, padx = 30, pady = 30)

        dogruYanlis = Label(soruPenceresi, text = "", font = ("Arial", 15))
        dogruYanlis.grid(column = 1, row = 2, padx = 20, pady = 20)

        buton1 = Button(soruPenceresi, text = "", height = 1, width = 11, font = ("Arial", 20), command = lambda: paket(1))
        buton2 = Button(soruPenceresi, text = "", height = 1, width = 11, font = ("Arial", 20), command = lambda: paket(2))
        buton3 = Button(soruPenceresi, text = "", height = 1, width = 11, font = ("Arial", 20), command = lambda: paket(3))

        buton1.grid(column = 0, row = 1)
        buton2.grid(column = 1, row = 1)
        buton3.grid(column = 2, row = 1)
        paket()

    else:
        pass

def bisi(tip_, bankaAdi_):
    soruPenceresi(tip_, bankaAdi_)

bankaSecimPenceresi()

mainloop()
