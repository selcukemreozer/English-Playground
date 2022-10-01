from tkinter import messagebox
from tkinter import *
import os
def kelimeBankasiDuzenle(master, isim):
    bankaKelimeEklemePenceresi(master=master, isim=isim, type="eski")

def kelimeBankasiOlustur(master, isim):
    if isim.replace(" ", "") != "":
        dosyaAdi = "kelime_bankalari/" + isim + ".txt"
        try:
            open(dosyaAdi, 'x')
            bankaKelimeEklemePenceresi(master=master, isim=isim, type="yeni")
            return isim

        except FileExistsError:
            w = Tk()
            w.withdraw() # <messagebox> penceresiz açılmıyor o yüzden penceresi olmadığında kendi küçük pencerisini
            # oluşturuyor. Bunu engellemek için yeni bir pencere oluşturup <withdraw()> ile onu gizledim.
            messagebox.showerror("Aynı İsim!", message="zaten bu isimde bir dosya var lütfen yeni bir isim kullanın.")
            w.destroy()
            return "" # none değeri hataya sebep oluyor

    else:
        messagebox.showwarning("Uyarı!", "Lütfen bankanıza bir isim koyun.")
        return "" # none değeri hataya sebep oluyor


def kelimeBankasiGuncelle(isim, ing_kelime, turkce_karsiligi, label, type="yeni"):
    if ing_kelime != '' and turkce_karsiligi != '':

        if type == "yeni":
            dosyaAdi = "kelime_bankalari/" + isim + ".txt"
        else:
            dosyaAdi = isim
        dosya = open(dosyaAdi, 'r')
        kelime = ing_kelime.replace("|", "*").replace("^", "*") + "^" + turkce_karsiligi.replace("|", "*").replace("^", "*") + "|"
        icerik = dosya.read()
        dosya.close()
        if kelime in icerik: # aynı kelimenin eklenmesini engelliyor
            messagebox.showinfo(title="uyarı", message="bu kelime zaten mevcut")

        else:
            dosya = open(dosyaAdi, 'a')
            dosya.write(kelime)
            label.config(text=("eklenen kelime >> " + ing_kelime + " : " + turkce_karsiligi))
            dosya.close()

    else:
        messagebox.showwarning(title="Uyarı!", message="Lütfen kutuları boş bırakmayın.")


def bankaKelimeEklemePenceresi(master, isim, type): # burada bağımsız bir pencere oluşturmak yerine
    # alt pencere oluşturuyor. Bu sayede <yeniBankaKelimeEklemePenceresi> açıkkan <master> pencerede
    # işlem yapılamayacak. Birçok hatanın önüne geçilecek.
    kelimesayiList = list()

    def multiTaskFunc():
        ingilizceKelime.delete(0, END)
        turkceKarsiligi.delete(0, END)
        kelimesayiList.append(1)

    def hepsiBirFonksiyon(event=None): # entry icin gerekli tüm fonksiyonları bir fonksiyonda topladım
        kelimeBankasiGuncelle(isim, ingilizceKelime.get(), turkceKarsiligi.get(), label=eklenenKelimeLabel, type=type)
        multiTaskFunc()
        ingilizceKelime.focus_set()

    def inglizceKelimeEntryFunc(event=None):
        turkceKarsiligi.focus_set()

    def pencere_kapat(senaryo="iptal"):
        if senaryo == "kaydet" and len(kelimesayiList) >= 4 and type=="yeni":
            messagebox.showinfo("Kaydedildi", "Dosya başarıyla kaydedildi")
            pencere.grab_release()
            pencere.destroy()

        elif senaryo == "kaydet" and type != "yeni":
            messagebox.showinfo("Kaydedildi", "Dosya başarıyla kaydedildi")
            pencere.grab_release()
            pencere.destroy()

        elif senaryo == "iptal":
            yesNo = messagebox.askyesno(
                title="Uyarı",
                message="kaydedilmemiş değişiklikler var çıkmak istediğinizden emin misiniz?"
            )

            if yesNo:
                if type == "yeni": # dosya yeni oluşturuluyorsa silecek. Düzenlenen dosyaları silmeyecek
                    dosyaAdi = "kelime_bankalari/" + isim + ".txt"
                    os.remove(dosyaAdi) # kullanıcı kaydetmek yerine kapatırsa oluşturulan dosya silinecek
                pencere.grab_release()
                pencere.destroy()
            else:
                pass


        elif len(kelimesayiList) < 4 and type == "yeni":
            message = "En az " + str(4 - len(kelimesayiList)) + " daha kelime eklemeniz lazım!"
            messagebox.showwarning(title="Uyarı",
                                  message=message)



    pencere = Toplevel(master)
    pencere.geometry("500x200+710+340")
    pencere.title("Kelime Bankası Düzenleyici")
    pencere.columnconfigure(0, weight=1)
    pencere.columnconfigure(1, weight=1)

    if len(isim) > 15:
        dosya_ismi = Label(pencere, text="dosya ismi:" + isim[:16]+"...", font=("Arial", 12))
    else:
        dosya_ismi = Label(pencere, text="dosya ismi:"+isim, font=("Arial", 12))

    eklenenKelimeLabel = Label(pencere, text="", font=("Arial", 11, "italic"))
    ekle_tusu = Button(pencere, text="Ekle", command=hepsiBirFonksiyon)

    kaydet_tusu = Button(pencere, text= "Kaydet",
                         command=lambda: pencere_kapat(senaryo="kaydet"))

    ingLabel = Label(pencere, text="İngilizce Kelime", font=("Arial", 11, "italic"))
    trLabel = Label(pencere, text="Türkçe karşılığı", font=("Arial", 11, "italic"))
    ingilizceKelime = Entry(pencere)
    turkceKarsiligi = Entry(pencere)

    dosya_ismi.grid(column=0, row=0)
    ingLabel.grid(column=0, row=1)
    trLabel.grid(column=1, row=1)
    ingilizceKelime.grid(column=0, row=2)
    turkceKarsiligi.grid(column=1, row=2)
    eklenenKelimeLabel.grid(column=0, row=3)
    ekle_tusu.grid(column=1, row=3, pady=7)
    kaydet_tusu.grid(column=1, row=4)
    turkceKarsiligi.bind('<Return>', hepsiBirFonksiyon)
    ingilizceKelime.bind('<Return>', inglizceKelimeEntryFunc)
    ingilizceKelime.focus_set() # pencere açıldığında imleç direkt <entry>e gidiyor. Fare kullanımına gerek kalmıyor
    # iptal_tusu.place(x=400, y=170)

    pencere.grab_set()
    pencere.protocol('WM_DELETE_WINDOW', pencere_kapat) # iptal tuşuyla değil de [X] tuşuyla kapatırsa
    # oluşturulan <txt> dosyasının silinmesini sağlıyor


