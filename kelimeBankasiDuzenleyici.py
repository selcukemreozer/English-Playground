from tkinter import messagebox
from tkinter import *
def kelimeBankasiOlustur(isim):
    dosyaAdi = "kelime_bankalari/" + isim + ".txt"

    try:
        open(dosyaAdi, 'x')
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

kelimeBankasiOlustur("a")

def yeniBankaKelimeEklemePenceresi():
    pencere = Tk()
    pencere.geometry("500x300")
    pencere.title("Kelime Bankası ")
    pencere.title("Kelime Bankası Düzenleyici")
    ingilizceKelime = Entry()
    pencere.columnconfigure(0, weight=1)
    pencere.columnconfigure(1, weight=1)

yeniBankaKelimeEklemePenceresi()
mainloop()