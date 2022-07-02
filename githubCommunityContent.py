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
def KELIMEBANKASI_EKLE(dosyaAdi, baslik, icerik, branchName):

    repo = g.get_repo("selcukemreozer/English-Playground")
    repo.create_file(dosyaAdi, baslik, icerik, branch=branchName)



