from bs4 import BeautifulSoup
import requests as rq
import random as rd
from kelimeBankasiDuzenleyici import kelimeBankasiOlustur
from kelimeBankasiDuzenleyici import kelimeBankasiDuzenle
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os.path

# import tkinter.ttk as ttk
# from icecream import ic

oncekiBanka = [""]
def RAKES_bankaDuzenleyici(tip, kelime_bankasi_ismi):

    ######################## bs4, requests, url ########################
    global hata # program herhangi bir hata ile karşılaştığında gerekli yerlerin çalışmasını durdurucak
    tum_kelimeler = str()

    try:
        hata = True

        if tip == "hazir":

            URL = "https://github.com/selcukemreozer/English-Playground/blob/main/kelime_bankalari/" + kelime_bankasi_ismi + ".txt"
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

        elif tip == "yerel":
            if os.path.exists("kelime_bankalari/"+kelime_bankasi_ismi+".txt") or os.path.exists(kelime_bankasi_ismi):
                if kelime_bankasi_ismi[0] != "C": # kısım4
                    results = open("kelime_bankalari/"+kelime_bankasi_ismi+".txt", "rt", encoding="cp1254")
                    # encoding="cp1254" kullanma sebebim türkçe karakter sıkıntısı çekmek
                    # https://stackoverflow.com/questions/62809169/how-to-read-turkish-chars-from-txt-file-in-python
                elif kelime_bankasi_ismi[0] == "C":
                    results = open(kelime_bankasi_ismi, "r+", encoding="cp1254")
                tum_kelimeler = results.read()

                if tum_kelimeler[-1] == "|": # str sonundaki eleman <"|"> ise hata çıkmaması için sondaki <"|"> kaldırıyor
                    tum_kelimeler = tum_kelimeler[:-1]
                else:
                    pass
            else:
                hata = False
                messagebox.showerror(title="Hata!", message="Dosya bulunamadı.")
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

    # print(f"silinecek eleman:{secim_}")
    return [ingilizceKelime, turkcesi, digerSecenek1, digerSecenek2, secim_]
####################################################################

########################       tkinter      ########################
def infoButton():
    message = "Geliştirici: S.Emre Özer\n"\
              "Versiyon: v1.0\n"\
              "RAKES, ingilizce öğrenmek isteyenlere yardımcı olmak için geliştirilmiş ücretsiz bir programdır."
    messagebox.showinfo(title="Hakkında", message=message)
def yardim():
    message = "Dosyanın direkt adını yazıp çalıştırabilirsiniz." \
              " Eğer bu işe yaramazsa ya da dosyanın adını tam bilmiyorsanız <Gözat> butonunu kullanabilirsiniz."
    messagebox.showinfo(title="Yardım", message=message)

def dosyaGezgini(yerel_banka_entry, label_name): # kısım4
    filename = filedialog.askopenfilename(initialdir="/kelime_bankalari",
                                          title="Dosya Seç",
                                          filetypes=(("Text Files", "*.txt*"), ("All Files", "*.*")))

    label_name.config(text=filename.split("/")[-1])
    yerel_banka_entry.delete(0, END)
    yerel_banka_entry.insert(0, filename)

def dosyaGezgini2(master):
    filename = filedialog.askopenfilename(initialdir="/kelime_bankalari",
                                          title="Dosya Seç",
                                          filetypes=(("Text Files", "*.txt*"), ("All Files", "*.*")))

    kelimeBankasiDuzenle(master=master, isim=filename)


def bankaOlustur(master, isim, entry_name, yerel_banka_entry):
    filename = kelimeBankasiOlustur(master=master, isim=isim)
    entry_name.delete(0, END)
    yerel_banka_entry.delete(0, END)
    yerel_banka_entry.insert(0, filename)
    file_exists = os.path.exists("kelime_bankalari/"+filename+".txt") # dosyanın var olup olmadığına bakıyor ama çalışmıyor

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
    bankaSecimPenceresi.geometry('700x500+610+190')
    bankaSecimPenceresi.columnconfigure(0, weight=1)
    bankaSecimPenceresi.columnconfigure(1, weight=1)
    bankaSecimPenceresi.columnconfigure(2, weight=2)

    butonFrame = LabelFrame(bankaSecimPenceresi, text="Hazır Kelime Bankaları", font=("Arial", 14))

    a1Buton = Button(butonFrame, text="a1", font=("Arial", 20),
                     command=lambda: [soruPenceresi("hazir", "a1"), QUIT()])

    a2Buton = Button(butonFrame, text="a2", font=("Arial", 20),
                     command=lambda: [soruPenceresi("hazir", "a2"), QUIT()])

    b1Buton = Button(butonFrame, text="b1", font=("Arial", 20),
                     command=lambda: [soruPenceresi("hazir", "b1"), QUIT()])

    b2Buton = Button(butonFrame, text="b2", font=("Arial", 20),
                     command=lambda: [soruPenceresi("hazir", "b2"), QUIT()])

    c1Buton = Button(butonFrame, text="c1", font=("Arial", 20),
                     command=lambda: [soruPenceresi("hazir", "c1"), QUIT()])

    c2Buton = Button(butonFrame, text="c2", font=("Arial", 20),
                     command=lambda: [soruPenceresi("hazir", "c2"), QUIT()])
    haftaninButonu = Button(bankaSecimPenceresi, text="Haftanın Kelimeleri", font=("Arial", 17),
                     command=lambda: [soruPenceresi("hazir", "haftanin_kelimeleri")])
    ##
    bankaOlusturCercevesi = LabelFrame(bankaSecimPenceresi, text='Kelime Bankası Oluştur', font=('Arial', 14))
    yerel_banka_ismi_entry = Entry(bankaOlusturCercevesi, width=20)
    yerel_banka_ismi = Label(bankaOlusturCercevesi, text="dosya adı:", font=("Arial", 12, "italic"))
    bankaOlusturButonu = Button(bankaOlusturCercevesi, text="olustur", font=("Arial", 13),
                                command=lambda: bankaOlustur(master=bankaSecimPenceresi,
                                                             isim=yerel_banka_ismi_entry.get(),
                                                             entry_name=yerel_banka_ismi_entry,
                                                             yerel_banka_entry=yerel_banka_bul_entry))
    ##
    yerelBankaCalistirCercevesi = LabelFrame(bankaSecimPenceresi, text='Yerel Banka ile Çalış', font=('Arial', 14))
    yerel_banka_bul_entry = Entry(yerelBankaCalistirCercevesi, width=20)
    dosyaAdiLabel = Label(yerelBankaCalistirCercevesi, text="", font=("Arial", 10, "italic"))
    yerelBankaAcButon = Button(yerelBankaCalistirCercevesi, text="Çalıştır", font=("Arial", 13), width=7,
                               command=lambda: [soruPenceresi("yerel", yerel_banka_bul_entry.get()), QUIT()])

    gozatButon = Button(yerelBankaCalistirCercevesi, text="Gözat", font=("Arial", 13, "italic"), width=6,
                        command=lambda: dosyaGezgini(yerel_banka_entry=yerel_banka_bul_entry, label_name=dosyaAdiLabel))

    yardimButon = Button(bankaSecimPenceresi, text="?", font=("Arial", 10, ["bold", "italic"]), height=5,
                         command=yardim)
    ##
    varOlanBankaDuzenleCercevesi = LabelFrame(bankaSecimPenceresi, text='Var Olan Bankayı Düzenle', font=('Arial',14))
    metin = Label(varOlanBankaDuzenleCercevesi, text="Ekleme yapmak istediğiniz dosyayı seçiniz", font=('Arial', 10, 'italic'))
    gozatButon2 = Button(varOlanBankaDuzenleCercevesi, text="Gözat", font=("Arial", 13, "italic"), width=13,
                         command=lambda: dosyaGezgini2(master=bankaSecimPenceresi))
    ##
    info_button = Button(bankaSecimPenceresi, text="Hakkında", font=('Italic', 10),
                        command=infoButton)
    butonFrame.place(x=50, y=40)
    a1Buton.grid(column=0, row=0, padx=20, pady=10)
    a2Buton.grid(column=1, row=0, padx=20, pady=10)
    b1Buton.grid(column=0, row=1, padx=20, pady=10)
    b2Buton.grid(column=1, row=1, padx=20, pady=10)
    c1Buton.grid(column=0, row=2, padx=20, pady=10)
    c2Buton.grid(column=1, row=2, padx=20, pady=10)
    haftaninButonu.place(x=47, y=310)

    bankaOlusturCercevesi.place(x=300, y=40)
    yerel_banka_ismi.grid(column=0, row=0, pady=5)
    yerel_banka_ismi_entry.grid(column=1, row=0, pady=7, padx=5)
    bankaOlusturButonu.grid(column=1, pady=5, padx=7, sticky=E)
    yerel_banka_ismi_entry.bind('<Return>', lambda event: bankaOlustur(
                                                   master=bankaSecimPenceresi,
                                                   isim=yerel_banka_ismi_entry.get(),
                                                   entry_name=yerel_banka_ismi_entry,
                                                   yerel_banka_entry=yerel_banka_bul_entry))

    yerelBankaCalistirCercevesi.place(x=300, y=190)
    yerel_banka_bul_entry.grid(column=0, row=0, pady=5)
    dosyaAdiLabel.grid(column=0, row=1, padx=5)
    yerelBankaAcButon.grid(column=1, row=1, padx=5, pady=5)
    gozatButon.grid(column=1, row=0)
    yerel_banka_bul_entry.bind("<Return>", lambda event:[soruPenceresi("yerel", yerel_banka_bul_entry.get()), QUIT()])
    yardimButon.place(x=533, y=200)

    varOlanBankaDuzenleCercevesi.place(x=300, y=340)
    gozatButon2.grid()
    metin.grid()
    info_button.place(x=490, y=450)

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
                    # print(f"silinecek eleman_:{silinecekEleman}")
                    kelimeBankasi.remove(silinecekEleman) # kullanıcı doğru cevap verirse kelşme geçici bankadan silinir
                    kalanKelimeLabel.config(text="Kalan Kelime:"+str(len(kelimeBankasi)))
                elif configKontrolcu:
                    if oncekiDogruCevap != "": # değişkene kısım3'te <""> değeri atanıyor o yüzden kırmızı bir çizgi
                        # oluşmasını engellemek için bu if koşulu kullanılıyor
                        dogruYanlis.config(text = oncekiDogruCevap, bg = '#FA5858') # FE2E2E FF4000
                else:
                    pass
                # print(len(kelimeBankasi))
            except NameError:
                butonHafiza = -1

            secenekler = secenekBelirleyici(kelimeBankasi)
            # print(kelimeBankasi)
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
            kelimeBankasi.remove(silinecekEleman) # bilinen son kelimeyi siliyor
            soruPenceresiMessage()

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
        soruPenceresi.geometry('1200x350+360+265')
        soruPenceresi.columnconfigure(0, weight=1)
        soruPenceresi.columnconfigure(1, weight=1)
        soruPenceresi.columnconfigure(2, weight=1)

        soru = Label(soruPenceresi, text="", bg="white", anchor=CENTER, font=("Arial", 25))
        kalanKelimeLabel = Label(soruPenceresi, text="Kalan Kelime:"+str(len(kelimeBankasi)), anchor=CENTER, font=("Arial", 15))
        soru.grid(column=0, row=0, padx=30, pady=30)

        dogruYanlis = Label(soruPenceresi, text="", font=("Arial", 15))


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

        kalanKelimeLabel.place(x=10, y=10)
        buton1.grid(column=0, row=1)
        buton2.grid(column=0, row=2)
        buton3.grid(column=0, row=3)
        dogruYanlis.place(x=80, y=300)
        cikisButonu.place(x=1051, y=300)
        anaMenuButonu.place(x=966, y=300)

        soonLabel = Label(soruPenceresi, text="Örnek cümle özelliği çok yakında!", font=("Arial", 13))
        # https://wordsinasentence.com/
        # https://dictionary.cambridge.org/tr/s%C3%B6zl%C3%BCk/ingilizce-t%C3%BCrk%C3%A7e/
        # https://www.tutorialspoint.com/how-to-create-a-hyperlink-with-a-label-in-tkinter#
        soonLabel.grid(column=1, row=0)
        paket()

        def soruPenceresiMessage():
            w = Tk()
            w.withdraw() # <messagebox> penceresiz açılmıyor o yüzden penceresi olmadığında kendi küçük pencerisini
                         # oluşturuyor. Bunu engellemek için yeni bir pencere oluşturup <withdraw()> ile onu gizledim.

            message = "kalan kelimeler:\n\n"

            for each in kelimeBankasi:
                word1, word2 = each.split('^')
                message += (word1 + " >> " + word2 + "\n")

            messagebox.showinfo(title='Başardın!', message=message)
            w.destroy()

    else:
        pass

bankaSecimPenceresi()
mainloop()
