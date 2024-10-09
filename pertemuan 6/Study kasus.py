Keys = {
    "Nama" : "yusuf",
    "Umur" : 18,
    "NIM" : 93,
    "Jurusan" : "Informatika",
    "ANgkatan" : 24
}
print("sebelum")
print(Keys)

print("fakultas : ", Keys.setdefault("fakultas", 70))
Keys["Jurusan"]
Keys.update({"Jurusan" : "sistem informasi"})
del Keys ["Nama"]
print(" ")
print("sesudah")
print(Keys)






nilai = {
    "matematika" : 90,
    "fisika" : 80,
    "biologi" : 80,
    "kimia" : 70
}
total = 0 
for i in nilai.values():
    total += i
print(f"total nilai : {nilai}")
print(f"rata rata nilai : {total/4}")