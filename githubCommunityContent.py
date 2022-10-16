from github import Github # https://pygithub.readthedocs.io/en/latest/introduction.html

access_token = "xxxx" # 9 Temmuza kadar geçerli sadece açık repolara erişim var.
g = Github(access_token)

# user = g.get_user("selcukemreozer")

"""
repo.create_file("test.txt", "başlık", "içerik", branch="community")

# community branchi bu program için oluşturulmuş bir branchdir.
# başlık ve dosya adı program tarafından numaralandırılabilir. Kimlik atamak gibi.
# içerik kısmında kullanıcıların oluşturduğu kelime bankaları olacak.(sadece string tipinde değişken kabul ediyor)
"""
"""
import time
>>> time.localtime()
time.struct_time(tm_year=2022, tm_mon=10, tm_mday=17, tm_hour=1, tm_min=2, tm_sec=38, tm_wday=0, tm_yday=290, tm_isdst=0)
>>> time.localtime()[1]
10
>>> type(time.localtime()[1])
<class 'int'>
"""
def KELIMEBANKASI_EKLE(dosyaAdi, baslik, icerik, branchName):

    repo = g.get_repo("selcukemreozer/English-Playground")
    repo.create_file(dosyaAdi, baslik, icerik, branch=branchName)



