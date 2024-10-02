print("1_______________________________________________________________________________________________")


makanan = ["bakso","sate","soto","nasi goreng","mi ayam","cumi goreng"],["teh","kopi","air"]
print("sebelum")
print(makanan)

print("sesudah")
for i in makanan :
    for j in i :
        print(j, end=" ")
        
        



print("2_____________________________________________________________________________________")



makanan = ["bakso","sate","soto","nasi goreng","mi ayam","cumi goreng"],["teh","kopi","air"]
print("sebelum")
print(makanan)

print("sesudah")
for i in makanan :
    if isinstance(i,list) :
        for j in i :
            print(j, end=" ")
            
            
            
print("3_____________________________________________________________________________________")


makanan = ["bakso","sate","soto","nasi goreng","mi ayam","cumi goreng"],["teh","kopi","air"]
print("sebelum")
print(makanan)

print("sesudah")
for i in makanan :
    if isinstance(i,list) :
        for j in i :
            print(j)
    else:
        print(i)
        
        
print("4_______________________________________________________________________________________")


print("5_______________________________________________________________________________________")