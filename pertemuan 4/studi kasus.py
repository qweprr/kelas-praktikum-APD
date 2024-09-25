# for i in range(10):
#     if i % i == 0 or i % 2 == 0:
#         continue
#     print(i)
    


while (True):
    angka = int(input("Masukkan angka: "))    
    if angka < 0:
        break
    total += angka
print("Total jumlah:", [total])