from tkinter import messagebox
from tkinter import *
import os

def kelimeBankasiOlustur(master, isim):
    if isim.replace(" ", "") != "":
        dosyaAdi = "kelime_bankalari/" + isim + ".txt"
        try:
            open(dosyaAdi, 'x')
            yeniBankaKelimeEklemePenceresi(master=master, isim=isim)

        except FileExistsError:
            w = Tk()
            w.withdraw() # <messagebox> penceresiz açılmıyor o yüzden penceresi olmadığında kendi küçük pencerisini
            # oluşturuyor. Bunu engellemek için yeni bir pencere oluşturup <withdraw()> ile onu gizledim.
            messagebox.showerror("Aynı İsim!", message="zaten bu isimde bir dosya var lütfen yeni bir isim kullanın.")
            w.destroy()

    else:
        messagebox.showwarning("Uyarı!", "Lütfen bankanıza bir isim koyun.")


def kelimeBankasiGuncelle(isim, ing_kelime, turkce_karsiligi):
    if ing_kelime != '' and turkce_karsiligi != '':
        dosyaAdi = "kelime_bankalari/" + isim + ".txt"
        dosya = open(dosyaAdi, 'a')
        dosya.write(ing_kelime + "^" + turkce_karsiligi + "|")
        dosya.close()

    else:
        messagebox.showwarning(title="Uyarı!", message="Lütfen kutuları boş bırakmayın.")


def yeniBankaKelimeEklemePenceresi(master, isim): # burada bağımsız bir pencere oluşturmak yerine
    # alt pencere oluşturuyor. Bu sayede <yeniBankaKelimeEklemePenceresi> açıkkan <master> pencerede
    # işlem yapılamayacak. Birçok hatanın önüne geçilecek.
    def pencere_kapat(senaryo="iptal"):
        if "kaydet" in senaryo:
            messagebox.showinfo("Kaydedildi", "Dosya başarıyla kaydedildi")
            pencere.grab_release()
            pencere.destroy()

        elif senaryo == "iptal":
            yesNo = messagebox.askyesno(
                title="Uyarı",
                message="kaydedilmemiş değişiklikler var çıkmak istediğinizden emin misiniz?"
            )

            if yesNo:
                dosyaAdi = "kelime_bankalari/" + isim + ".txt"
                os.remove(dosyaAdi) # kullanıcı kaydetmek yerine kapatırsa oluşturulan dosya silinecek
                pencere.grab_release()
                pencere.destroy()
            else:
                pass



    pencere = Toplevel(master)
    pencere.geometry("500x200+710+340")
    pencere.title("Kelime Bankası Düzenleyici")
    pencere.columnconfigure(0, weight=1)
    pencere.columnconfigure(1, weight=1)

    dosya_ismi = Label(pencere, text="dosya ismi:"+isim, font=("Arial", 12))
    ekle_tusu = Button(pencere, text="Ekle",
                       command=lambda: kelimeBankasiGuncelle(isim, ingilizceKelime.get(), turkceKarsiligi.get()))

    kaydet_tusu = Button(pencere, text= "Kaydet",
                         command=lambda: pencere_kapat(senaryo="kaydet"))

    # iptal_tusu = Button(pencere, text="iptal", command=pencere_kapat)
    ingLabel = Label(pencere, text="İngilizce Kelime", font=("Arial", 11, "italic"))
    trLabel = Label(pencere, text="Türkçe karşılığı", font=("Arial", 11, "italic"))
    ingilizceKelime = Entry(pencere)
    turkceKarsiligi = Entry(pencere)

    dosya_ismi.grid(column=0, row=0)
    ingLabel.grid(column=0, row=1)
    trLabel.grid(column=1, row=1)
    ingilizceKelime.grid(column=0, row=2)
    turkceKarsiligi.grid(column=1, row=2)
    ekle_tusu.grid(column=1, row=3, pady=7)
    kaydet_tusu.grid(column=1, row=4)
    # iptal_tusu.place(x=400, y=170)

    pencere.grab_set()
    pencere.protocol('WM_DELETE_WINDOW', pencere_kapat) # iptal tuşuyla değil de [X] tuşuyla kapatırsa
    # oluşturulan <txt> dosyasının silinmesini sağlıyor

"""    
    pencere = Tk()
    pencere.geometry("500x300")
    pencere.title("Kelime Bankası ")
    pencere.title("Kelime Bankası Düzenleyici")
    ingilizceKelime = Entry()
    pencere.columnconfigure(0, weight=1)
    pencere.columnconfigure(1, weight=1)
"""

