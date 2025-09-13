# 1. Deklarasi variabel dan tipe data

a = str("Muhammad")
a1 = str("Trio")
a2 = str("Novrian")
b = int(2)
c = float(7.0)
d = bool(True)
e = list([4, "apple", "manggo", 3.5, True])

# cek
print(
    f"Tipe datanya:\n"
    f"    tipe data dari 'a' {type(a)}\n"
    f"    tipe data dari 'b' {type(b)}\n"
    f"    tipe data dari 'c' {type(c)}\n"
    f"    tipe data dari 'd' {type(d)}\n"
    f"    tipe data dari 'e' {type(e)}\n"
)


# 2. Manipulasi string

# tampilkan teks menggunakan string


# menggabungkan string
print(f"Gabungin string : \nGabung :{a + " " + a1 + " " + a2}")
# menghitung panjang
print(f"panjangnya a :{len(a)}")
# manipulasi ke uppercase
print(f"Uppercase a :{a.upper()}")
# manipulasi ke r
print(f"Lowercase a :{a.lower()}, \n")


# 3. Operasi Matematikan Sederhana

# gabung dari tambah sampai ke sisa bagi
print(
    f"Operasi matematika:\n"
    f" 2 + 2 : {b + b}\n"
    f" 2 - 2 : {b - b}\n"
    f" 2 * 2 : {b * b}\n"
    f" 2 / 2 : {b / b}\n"
    f" 2 // 2 : {b // b}\n"
    f" 7.0 % 4 : {c % e[0]}\n"
)


# 4. List dan akses elemen
print("Menampilkan dan manipulasi list :")
# tampilkan manggo
print(f"ini list awal :{e} \n"
      f"tampilin list ke 3 (manggo) :{e[2]}")
# tambahkan item baru
e.append("pisang")
print(f"pas ditambahin pisang : {e}")
# hapus pisang
e.remove("apple")
print(f"pas apple dihapus :{e} \n")

# 5. Input nama user terus di print
print("Input nama dan umur dong")
nama = input("Masukkan nama :")
umur = int(input("Masukkan umur :"))

print(f"Halo, {nama}")
if umur >= 20:
    print(f"{umur} tahun! Kamu udah lumayan tua ya!")
else:
    print(f"{umur} tahun! Kamu masih muda banget!")
