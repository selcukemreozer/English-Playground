from bs4 import BeautifulSoup
import requests as rq
import random as rd
from kelimeBankasiDuzenleyici import *
from tkinter import *
from tkinter import messagebox
from icecream import ic

oncekiBanka = [""]
def RAKES_bankaDuzenleyici(tip, kelime_bankasi_ismi):

    ######################## bs4, requests, url ########################
    global hata # program herhangi bir hata ile karşılaştığında gerekli yerlerin çalışmasını durdurucak
    tum_kelimeler = str()

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

                elif each == len(results)-1:
                    hata = False
                    messagebox.showerror(title="HATA!", message="Bir hata meydana geldi ve kelime bankasına erişemedik."
                                                                "\nBu hata devam ederse lütfen geliştiriciyle iletişime"
                                                                " geçin.")
                    break
                else:
                    pass

        elif tip == "topluluk":
            results = open("kelime_bankalari/"+kelime_bankasi_ismi+".txt", "r+", encoding="utf-8")
            tum_kelimeler = results.read()

            if tum_kelimeler[-1] == "|": # str sonundaki eleman <"|"> ise hata çıkmaması için sondaki <"|"> kaldırıyor
                tum_kelimeler = tum_kelimeler[:-1]
            else:
                pass
        else:
            pass

        kelimeListesi = tum_kelimeler.split('|')
        oncekiBanka.remove(oncekiBanka[0])
        oncekiBanka.append(kelime_bankasi_ismi)
        return kelimeListesi

    except FileNotFoundError:
        messagebox.showerror(title="HATA! >> warning", message="Aradığınız dosya bulunamadı!")
        hata = False
        # return [":"] # dosya bulunamadı hatası aldığında secenekBelirleyici'ye değer döndürmesi hataya sebep oluyor
                  # o yüzden boş liste döndürüyor >> hata değişkeniyle hallettik

    except rq.exceptions.ConnectionError:
        messagebox.showerror(title="Bağlantı Hatası!", message="İnternet baplantısı sağlanamadı!")
        hata = False
        # return [":"] # dosya bulunamadı hatası aldığında secenekBelirleyici'ye değer döndürmesi hataya sebep oluyor
                  # o yüzden boş liste döndürüyor >> hata değişkeniyle hallettik
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
    secim_ = rd.choice(kelimeBankasi).split('^') olsaydı >> secim_ = ['red','kırmızı']
    olacaktı. Ve

    digerSecenek1 = 'kırmızı:red'
    olsaydı >> if digerSecenek1 == secim_:

    bunu fark etmeyecekti çünkü:

    if 'kırmızı:red' == ['red','kırmızı'] >> False döndürecekti.

    Ve random fonksiyonu aynı değeri dödürene kadar bu hata fark edilemeyecekti.
    :return:
    """
    secim_ = rd.choice(kelimeBankasi)
    ingilizceKelime, turkcesi = secim_.split('^')

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

    print(f"silinecek eleman:{secim_}")
    return [ingilizceKelime, turkcesi, digerSecenek1, digerSecenek2, secim_]
####################################################################

########################       tkinter      ########################
def bankaSecimPenceresi():
    global hata

    def QUIT(): # eğer hata varsa kelime sorucu açılmayacak o yüzden Banka Seçim Penceresi kapanmasın
        if hata:
            bankaSecimPenceresi.destroy()
        else:
            pass
    bankaSecimPenceresi = Tk()
    bankaSecimPenceresi.resizable(False, False)
    bankaSecimPenceresi.title('RAKES')
    bankaSecimPenceresi.geometry('700x500+710+290')
    bankaSecimPenceresi.columnconfigure(0, weight=1)
    bankaSecimPenceresi.columnconfigure(1, weight=1)
    bankaSecimPenceresi.columnconfigure(2, weight=2)

    a1Buton = Button(bankaSecimPenceresi, text="a1", font=("Arial", 20),
                     command=lambda: [soruPenceresi("topluluk", "beta"), QUIT()])

    a2Buton = Button(bankaSecimPenceresi, text="a2", font=("Arial", 20),
                     command=lambda: [soruPenceresi("hazir", "a2"), QUIT()])

    b1Buton = Button(bankaSecimPenceresi, text="b1", font=("Arial", 20),
                     command=lambda: [soruPenceresi("hazir", "b1"), QUIT()])

    b2Buton = Button(bankaSecimPenceresi, text="b2", font=("Arial", 20),
                     command=lambda: [soruPenceresi("hazir", "b2"), QUIT()])

    c1Buton = Button(bankaSecimPenceresi, text="c1", font=("Arial", 20),
                     command=lambda: [soruPenceresi("hazir", "c1"), QUIT()])

    c2Buton = Button(bankaSecimPenceresi, text="c2", font=("Arial", 20),
                     command=lambda: [soruPenceresi("hazir", "c2"), QUIT()])

    butonBeta = Button(bankaSecimPenceresi, text="yeni kelime bankasi olustur", font=("Arial", 20),
                       command=lambda: kelimeBankasiOlustur("name"))

    a1Buton.grid(column=0, row=0, sticky=E, padx=5, pady=50)
    a2Buton.grid(column=1, row=0, sticky=W, padx=5, pady=50)
    b1Buton.grid(column=0, row=1, sticky=E, padx=5, pady=5)
    b2Buton.grid(column=1, row=1, sticky=W, padx=5, pady=5)
    c1Buton.grid(column=0, row=2, sticky=E, padx=5, pady=50)
    c2Buton.grid(column=1, row=2, sticky=W, padx=5, pady=50)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
def deleter(): # ana menuya dönüp geri geldiğinde önceki doğru cevap değişiyordu o yüzden <deleter()> fonksiyonu
               # her ana menüye dönüşte önceki doğru cevabı siliyor. Bu sayede tıklamadığın soruların cevabını görmicen
    global oncekiDogruCevap
    del oncekiDogruCevap

def soruPenceresi(tip, kelimeBankasi_ismi):
    global hata
    global oncekiKelimeBankasi
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
    if oncekiBanka[0] != kelimeBankasi_ismi: # kullanıcı menuye dönünce tekrar aynı bankayı seçerse web kazıma yapmaz
        kelimeBankasi = RAKES_bankaDuzenleyici(tip, kelimeBankasi_ismi) # bu satır, kısım <if hata:>'nın üstünde
    # olmalı çünkü hata değişkenine değer atıyor
    # ayrıca bu satır <paket()> fonksiyonunun dışında olmalı çünkü paket fonksiyonu özyinelemeli bir fonksiyon
    # her çağrıldığında tekrar web kazıma yapması programı çok hantallaştırıyor
        oncekiBanka.remove(oncekiBanka[0])
        oncekiBanka.append(kelimeBankasi_ismi)
        oncekiKelimeBankasi = kelimeBankasi
    else:
        kelimeBankasi = oncekiKelimeBankasi

    def paket(cevap_butonNo = 0, configKontrolcu = True):
        # kısım2 ve kısım2.1'de <paket()> çağırılıyor ama <Label:dogruYanlis> ataması gerçekleşmediği için sonsuz
        # hata döngüsüne giriyor. bunu engellemek için <configKontrolcu> parametresi kullanılıyor. Varsayılan değer:True
        # kısım1'de <paket()> alacak bir cevap_butonNo değerine sahip değildir
                                  # o yüzden cevap_butonNo = 0
        global silinecekEleman
        global oncekiDogruCevap
        global butonHafiza
        global oncekiKelime_  # global değişken olmalı çünkü oncekiKelime_ 'yi aklında tutuyor
        # global değişkene ihtiyaç duydum çünkü fonksiyonu tuşla çağırdığımız için
        # return değişkenleri saklamanın yolunu bulamadım

        if hata and len(kelimeBankasi) >= 4:

            try:
                if butonHafiza == cevap_butonNo and configKontrolcu:
                    dogruYanlis.config(text = "BRAVO!", bg = '#2EFE2E')
                    print(f"silinecek eleman_:{silinecekEleman}")
                    kelimeBankasi.remove(silinecekEleman) # kullanıcı doğru cevap verirse kelşme geçici bankadan silinir
                elif configKontrolcu:
                    if oncekiDogruCevap != "": # değişkene kısım3'te <""> değeri atanıyor o yüzden kırmızı bir çizgi
                        # oluşmasını engellemek için bu if koşulu kullanılıyor
                        dogruYanlis.config(text = oncekiDogruCevap, bg = '#FA5858') # FE2E2E FF4000
                else:
                    pass
                print(len(kelimeBankasi))
            except NameError:
                butonHafiza = -1

            secenekler = secenekBelirleyici(kelimeBankasi)
            print(kelimeBankasi)
            dogruCevap = secenekler[1]
            secenek1 = secenekler[2].split('^')[1]
            secenek2 = secenekler[3].split('^')[1]
            silinecekEleman = secenekler[4] # doğru cevaplanması halinde bilinen kelime silinecek

            try:
                if oncekiKelime_ == secenekler[0] and configKontrolcu: # kısım1
                    # önceki kelime ile yeni kelime aynı ise özyineleme ile
                    # tekrar yeni bir kelime çekiliyor
                    # print(f"tekrar:{oncekiKelime_}:{secenekler[0]}") >> KONTROL SİSTEMİ
                    paket()

                elif configKontrolcu:
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

                else:
                    pass


            except NameError: # kısım2
                # global değişkene ilk seferde bir şey atayamazdım çünkü fonksiyon çağrıldığında
                # hep aynı atama gerçekleşecekti(örn. oncekiKelime_ = "") ve değişken görevini
                # yerine getiremeyecekti.
                oncekiKelime_ = ""
                paket(configKontrolcu=False)
                # oncekiKelime_ ilk değerini kazandıktan sonra özyinelme ile tekrar bir değer
                # ataması gerçekleşiyor

        elif hata and len(kelimeBankasi) == 3:
            print(kelimeBankasi)
            kelimeBankasi.remove(silinecekEleman) # bilinen son kelimeyi siliyor
            # mesaj = "kelime bankasını başarıyla tamamladınız.\nKalan kelimeler:"\
                    # +"\n"+kelimeBankasi[0]+"\n"+kelimeBankasi[1]
            # print(type(mesaj))
            # messagebox.showinfo(title='Başardın!', message=str(kelimeBankasi)) # fazladan pencere açıyor!
            soruPenceresiMessage('Başardın!')
            try:
                soruPenceresi.destroy()
            except:
                pass

            oncekiDogruCevap = "" # kısım3
            oncekiBanka.remove(oncekiBanka[0])
            oncekiBanka.append("")
            bankaSecimPenceresi()

        else:
            pass

    paket(configKontrolcu=False) # kısım2.1

    if hata and len(kelimeBankasi) >= 4:
        soruPenceresi = Tk()
        soruPenceresi.resizable(False, False)
        soruPenceresi.title('RAKES')
        soruPenceresi.geometry('1200x400+360+290')
        soruPenceresi.columnconfigure(0, weight=1)
        soruPenceresi.columnconfigure(1, weight=1)
        soruPenceresi.columnconfigure(2, weight=1)

        soru = Label(soruPenceresi, text="", bg="white", anchor=CENTER, font=("Arial", 25))
        soru.grid(column=0, row=0, padx=30, pady=30)

        dogruYanlis = Label(soruPenceresi, text="", font=("Arial", 15))
        dogruYanlis.grid(column=0, row=1, padx=20, pady=20)

        buton1 = Button(soruPenceresi, text="", height=1, width=30, font=("Arial", 20),
                        command = lambda: paket(1))
        buton2 = Button(soruPenceresi, text="", height=1, width=30, font=("Arial", 20),
                        command = lambda: paket(2))
        buton3 = Button(soruPenceresi, text="", height=1, width=30, font=("Arial", 20),
                        command = lambda: paket(3))
        cikisButonu = Button(soruPenceresi, text="çıkış", height=1, width=3, font=("Arial", 12),
                        command=lambda: soruPenceresi.destroy())
        anaMenuButonu = Button(soruPenceresi, text="Ana Menü", height=1, width=8, font=("Arial", 12),
                        command=lambda: [soruPenceresi.destroy(), bankaSecimPenceresi(), deleter()])

        buton1.grid(column=0, row=2)
        buton2.grid(column=0, row=3)
        buton3.grid(column=0, row=4)
        cikisButonu.place(x=451, y=350)
        anaMenuButonu.place(x=366, y=350)

        soonLabel = Label(soruPenceresi, text="Örnek cümle özelliği çok yakında!", font=("Arial", 13))
        # https://wordsinasentence.com/
        # https://dictionary.cambridge.org/tr/s%C3%B6zl%C3%BCk/ingilizce-t%C3%BCrk%C3%A7e/
        # https://www.tutorialspoint.com/how-to-create-a-hyperlink-with-a-label-in-tkinter#
        soonLabel.grid(column=1, row=0)
        paket()

        def soruPenceresiMessage(type):
            w = Tk()
            w.withdraw() # <messagebox> penceresiz açılmıyor o yüzden penceresi olmadığında kendi küçük pencerisini
                         # oluşturuyor. Bunu engellemek için yeni bir pencere oluşturup <withdraw()> ile onu gizledim.
            if type == "Başardın!":
                message = "kalan kelimeler:\n\n"

                for each in kelimeBankasi:
                    word1, word2 = each.split('^')
                    message += (word1 + " >> "+ word2 + "\n")

                messagebox.showinfo(title='Başardın!', message=message)
                w.destroy()

    else:
        pass

bankaSecimPenceresi()
mainloop()
