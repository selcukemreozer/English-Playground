from github import Github

access_token = "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"
g = Github(access_token)

# user = g.get_user("selcukemreozer")
repo = g.get_repo("selcukemreozer/English-Playground")
"""
repo.create_file("test.txt", "başlık", "içerik", branch="community")

# community branchi bu program için oluşturulmuş bir branchdir.
# başlık ve dosya adı program tarafından numaralandırılabilir. Kimlik atamak gibi.
# içerik kısmında kullanıcıların oluşturduğu kelime bankaları olacak.(sadece string tipinde değişken kabul ediyor)

"""




