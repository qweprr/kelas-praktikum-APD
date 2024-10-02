nama = ["shandy",106,True,
        ["andi",142],3.96,
        [123,"YUSUF",False,3.21],
        "bagas"]
print(nama[4])

print("1--------------------------------")

matkul = ["APD",
          "APL",
          "matkul",
          "jarkom",
          "basdat",
          "STRUKDAT",
          "kalkulus"
          "PTI",
          "WEB"
]
# print(nama[1])
print(matkul[1])

print("2--------------------------------")

makanan = ["bakso","sate","soto"]
print("sebelum: ")
# makanan.append("nasi goreng")
print("sesudah: ")
# print(makanan)
makanan.insert(1,"nasi goreng")
print(makanan)

print("3--------------------------------")

makanan = ["bakso","sate","soto"]
print("sebelum: ")
# makanan.append("nasi goreng")
print("sesudah: ")
# print(makanan)
# makanan.insert(1,"nasi goreng")
# print(makanan)
makanan[0] = ["nasi goreng","bebek"]
print(makanan)

print("4--------------------------------")

makanan = ["bakso","sate","soto","nasi goreng","mi ayam","cumi goreng"]
print("sebelum: ")
print(makanan)
# makanan.append("nasi goreng")
print("sesudah: ")
del makanan[2]
# print(makanan)
# makanan.insert(1,"nasi goreng")
# print(makanan)
# makanan[0] = ["nasi goreng","bebek"]
print(makanan)

print("5--------------------------------")

makanan = ["bakso","sate","soto","nasi goreng","mi ayam","cumi goreng"]
print("sebelum: ")
print(makanan)
# makanan.append("nasi goreng")
print("sesudah: ")
data = makanan.pop(5)
print(makanan)
print(data)
# print(makanan)
# makanan.insert(1,"nasi goreng")
# print(makanan)
# makanan[0] = ["nasi goreng","bebek"]
# print(makanan)

print("6--------------------------------")

makanan = ["bakso","sate","soto","nasi goreng","mi ayam","cumi goreng"]
print("sebelum: ")
print(makanan)
# makanan.append("nasi goreng")
print("sesudah: ")
makanan.clear()
print(makanan)
# data = makanan.pop(5)
# print(makanan)
# print(data)
# print(makanan)
# makanan.insert(1,"nasi goreng")
# print(makanan)
# makanan[0] = ["nasi goreng","bebek"]
# print(makanan


print("7--------------------------------")


minuman = ["es buah","es teler","es jambu","jus mangga","es sirsak","es teh","jus alpukat"]
print("sebelum")
print(minuman)

print("sesudah")
del minuman[2]
# makanan.insert(6,"air")
minuman[5] = "air putih"
minuman.insert(0,"jus tomat")
print(minuman)

print("8--------------------------------")

makanan = ["bakso","sate","soto","nasi goreng","mi ayam","cumi goreng"]
print("sebelum")
print(makanan)

print("sesudah")
for i in makanan :
    print(i, end=", ")
    
    
    
  
print("9_______________________________________________________________________________________________")


makanan = ["bakso","sate","soto","nasi goreng","mi ayam","cumi goreng"],["teh","kopi","air"]
print("sebelum")
print(makanan)

print("sesudah")
for i in makanan :
    for j in i :
        print(j, end=" ")
        
        



print("10_______________________________________________________________________________________________")


makanan = ["bakso","sate","soto","nasi goreng","mi ayam","cumi goreng"],["teh","kopi","air"]
print("sebelum")
print(makanan)

print("sesudah")
for i in makanan :
    if isinstance(i,list) :
        for j in i :
            print(j, end=" ")



print("11_______________________________________________________________________________________________")



print("12_______________________________________________________________________________________________")