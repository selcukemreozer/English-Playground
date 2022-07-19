from tkinter import messagebox
from tkinter import *
import os
def kelimeBankasiOlustur(master, isim):
    dosyaAdi = "kelime_bankalari/" + isim + ".txt"

    try:
        open(dosyaAdi, 'x')
        yeniBankaKelimeEklemePenceresi(master=master, isim=isim)
    except FileExistsError:
        w = Tk()
        w.withdraw() # <messagebox> penceresiz açılmıyor o yüzden penceresi olmadığında kendi küçük pencerisini
                         # oluşturuyor. Bunu engellemek için yeni bir pencere oluşturup <withdraw()> ile onu gizledim.
        messagebox.showerror(title="Aynı İsim!", message="zaten bu isimde bir dosya var lütfen yeni bir isim kullanın.")
        w.destroy()
        print("zaten bu isimde bir dosya var lütfen yeni bir isim kullanın.")


def kelimeBankasiGuncelle(isim, ingKelime, turkceKarsiligi):
    dosyaAdi = "kelime_bankalari/" + isim + ".txt"

    dosya = open(dosyaAdi, 'a')
    dosya.write(ingKelime + "^" + turkceKarsiligi + "|")
    dosya.close()



def yeniBankaKelimeEklemePenceresi(master, isim): # burada bağımsız bir pencere oluşturmak yerine
    # alt pencere oluşturuyor. Bu sayede <yeniBankaKelimeEklemePenceresi> açıkkan <master> pencerede
    # işlem yapılamayacak. Birçok hatanın önüne geçilecek.
    def pencere_kapat(senaryo="iptal"):
        if senaryo == "kaydet":
            pass
        elif senaryo == "iptal":
            dosyaAdi = "kelime_bankalari/" + isim + ".txt"
            os.remove(dosyaAdi)
        pencere.grab_release()
        pencere.destroy()

    pencere = Toplevel(master)
    pencere.geometry("500x300")
    pencere.title("Kelime Bankası Düzenleyici")
    pencere.columnconfigure(0, weight=1)
    pencere.columnconfigure(1, weight=1)

    dosya_ismi = Label(pencere, text=isim)
    kapat_tusu = Button(pencere, text="iptal", command=pencere_kapat)
    dosya_ismi.grid()
    ingilizceKelime = Entry()
    kapat_tusu.grid()

    pencere.grab_set()

"""    
    pencere = Tk()
    pencere.geometry("500x300")
    pencere.title("Kelime Bankası ")
    pencere.title("Kelime Bankası Düzenleyici")
    ingilizceKelime = Entry()
    pencere.columnconfigure(0, weight=1)
    pencere.columnconfigure(1, weight=1)
"""

