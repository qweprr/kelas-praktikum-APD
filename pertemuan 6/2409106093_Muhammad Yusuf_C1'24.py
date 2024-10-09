# daftar_buku = {
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# print("="*20)

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }

# print(Biodata["KRS"][0:])

# print("="*20)

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }

# print(Biodata["Social Media"]["Discord"])


# print("="*20)


# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = {"nama" : {123 : "informatika"}})
# print(games['Valorant']['nama'][123])
# print(games["Pokemon"])

# print("="*20)

# Games = {
#     "Game1": "PUBG Mobile",
#     "Game2": "Mobile Legends",
#     "Game3": {
#         "nama" : "COC",
#         "genre" : "Strategy"
#     }
# }
# print((Games.get('Game3')).get('genre'))


# print("="*20)


# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
#     print("")
# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")



# print("="*20)


# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller", "Rush Hour" : "Comedi"})
# #Setelah Ditambah
# print(Film)


# print("="*20)


# data = {
#     "Nama" : "Aldy",
#     "Umur" : 19,
#     "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# del data["Nama"]

# #Setelah diubah
# print(data)
# #memanggil data yang telah dihapus
# print(data.get("Nama"))


# print("="*20)


# data = {
#     "Nama" : "Aldy",
#     "Umur" : 19,
#     "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# cache = data.pop("Nama")
# #Setelah dihapus
# print(data)
# #memanggil data yang telah dihapus pada dictionary
# print(data.get("Nama"))
# #memanggil data yang telah dihapus pada variabel cache
# print(cache)

# print("="*20)

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller", "Rush Hour" : "Comedi"})
# #Setelah Ditambah
# print(Film)
# # Sebelum Ditambah


# print(Film)
# simpan = Film.pop('Hours')
# # Film.clear
# print(Film)
# Film["Hours"] = simpan
# print(Film)


# print("="*20)


# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# print("Jumlah Data = ", len(data))



# Buku = {
#     "No Longer Human" : "Osamu Dazai",
#     "Harry Potter" : "J.K. Rowlings",
#     "Hamlet" : "William Shakespeare"
# }
# pinjam = Buku.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)


key = "apel", "jeruk", "mangga"
value = 1
buah = dict.fromkeys(key, value)
print(buah)


print("="*20)


Nilai = {
    "Matematika" : 80,
    "B. Indonesia" : 90,
    "B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai Kimia : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)



print("="*20)



Musik = {
    "The Chainsmoker" : ["All we Know", "The Paris"],
    "Alan Walker" : ["Alone", "Lily"],
    "Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
    for song in j:
        print(song)
print("")