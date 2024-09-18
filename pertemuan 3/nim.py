nim = int(input("Masukkan nim Anda : " ))
hasil = "kelas a" if nim >= 1 and nim <= 10 else "kelas b"  if nim >= 11 and nim <= 20 else "kelas c" if nim >= 21 and nim <= 30 else "anda bukan mahasiswa unmul"
print(hasil)


nim = int(input("Masukkan nim Anda : " ))
if nim >= 1 and nim <= 20 :
    if nim >= 1 and nim <= 10 :
        print("kelas c1")
    else:
        print("kelas c2")
elif nim >= 21 and nim <= 40 :
    if nim >= 21 and nim <= 30 :
        print("kelas b1")
    else :
        print("kelas b2")
elif nim >= 41 and nim <= 60 :
    if nim >= 41 and nim <= 50 :
        print("kelas a1")
    else :
        print("kelas a2")
else :
    print("anda bukan mahasiswa informatika")
