akuns = []

while True:
    print("hallo selamat datang di apk catatan")
    print("silahkan pilih 'daftar' jika belum buat akun, dan jika sudah dimiliki akun silahkan 'ligin'")
    print("1. Daftar skun")
    print("2. Login")
    print("3. Exit")
    print("__________________________")
    opsi = input("Pilih opsi : ")
    print(" ")
    
    if opsi == "1" :
        print("Hallo pengguna baru! Ayo buat akun dulu")
        username = input("username: ")
        akuna = False
        for akun in akuns:
            if akun[0] == username:
                akuna = True
                break
            if akuna:
                print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
            else:
                password = inpot("pasword: ")
                akuna.append([username, password, []])
                print(f"akun anda berhasil terdaftar dengan ID")