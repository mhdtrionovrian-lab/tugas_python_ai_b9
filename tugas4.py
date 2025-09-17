# 1. List akses & manipulasi

# buat list dengan >= 6 dengan type data campuran (angka/string)
print("List :Muhammad Trio Novrian, 21, Palembang, Main game, 5, False \n")
data_diri = ["Muhammad Trio Novrian", 21, "Palembang", "Main game", 5, False]

# tampilkan elemen pertama dan terakhir, slicing [start :stop: step]
print(
    f"Tampilin data pertama dan terakhir \nData Pertama dan terakhir :{data_diri[0:6:5]}\n")

# lakukan: append(), insert(), extend(), pop(), remove() lalu tampilkan sebelum & sesudah.

# append()
print(f"Before append :{data_diri}")
print("Masukkan data 'Aselole' di akhir")
data_diri.append("Aselole")
print(f"After append :{data_diri} \n")

# insert
print(f"Before insert :{data_diri}")
print("Masukkan data 'Kece' di urutan ke 2")
data_diri.insert(1, "Kece")
print(f"After insert :{data_diri} \n")

# extend
print(f"Before extend :{data_diri}")
print("Masukkan data 'gua', 'kece', 'dari lahir' di urutan terakhir")
data_diri.extend(["gua", "kece", "dari lahir"])
print(f"After extend :{data_diri} \n")

# pop
print(f"Before pop:{data_diri}")
x = data_diri.pop(3)
print(f"Item yang mau di hapus :{x}")
print(f"After pop :{data_diri} \n")

# remove
print(f"Before remove:{data_diri}")
print(f"Item yang mau di hapus berdasarkan value :{data_diri[3]}")
data_diri.remove("Main game")
print(f"After remove :{data_diri} \n")


# 2 Tuple – immutability & unpacking

# Buat tupple dengan >= 5 elemen
lesson = ("Matematika", "Bahasa", "English", "Programming", "Seni")
print(f"Buatlah list Tupple(Immutable/gabisa diubah)\nLesson:{lesson}")

# Berapa elemen yang kamu buat?
print(f"\nBerapa banyak datanya :{len(lesson)}")

# Ambil elemen tertentu
print(f"Pelajaran kesukaan :{lesson[1]}")
print(f"Pelajaran tidak kesukaan :{lesson[4]}\n")

# Unpacking dah tuh anunya (Tuple-nya)

# BONGKAR!!!
a, b, c, * rest = lesson
# print("cek cek bongkar", a, b, c, d, e)

# Baru deh kita bisa bongkar, coba 3 item deh pake *rest
print(f"Aku mau bongkar 3 item terakhir :{c, * rest}\n"
      f"Bongkar 3 item awal juga :{a, b, c}\n"
      )

# Set – keunikan & operasi himpunan

# Buat dua set dengan beberapa elemen yang saling tumpang tindih.
set_1 = {'a', "b", 'c', 'd', 'e'}
set_2 = {'d', 'e', 'f', 'g', 'h'}
print(f"Buat dua set tumpang tindih\n\n"
      f"Data set_1 ={set_1}\n"
      f"Data set_2 ={set_2}\n"

      )

# Tampilkan: union (|), intersection (&), difference (-), symmetric_difference (^).
# union
print(f"Ini union :{set_1 | set_2}\n")

# intersection
print(f"Ini intersection :{set_1 & set_2}\n")

# difference
print(f"Ini diference :{set_1 - set_2}\n")

# symetric_difference
print(f"Ini symetric_diference :{set_1 ^ set_2}\n")

# Tunjukkan bahwa duplikat otomatis hilang.
print("Perhatikan apakah ada duplikat? Ya tidak!\n")

# Dictionary – key/value dasar
# Buat dict data mahasiswa: nama, nim, angkatan, kota.
data_mahasiswa = {
    "nama": "Muhammad Trio Novrian",
    "nim": "062240723002",
    "angkatan": 2022,
    "kota": "Palembang"
}
print("Data dictionay mahasiwa\n",
      f"Ini dia datanya : {data_mahasiswa}"
      )

# Operasi: tambah key baru, ubah nilai key, hapus key.
# Tambah key baru
data_mahasiswa["Hobi"] = "Membaca"
print(f"Setelah menambah key :{data_mahasiswa}")

# Ubah nilai key
data_mahasiswa["Hobi"] = "Bermain Valorant"
print(f"Setelah ganti nilai key :{data_mahasiswa}")

# hapus key
del data_mahasiswa["Hobi"]
print(f"Setelah hapus key :{data_mahasiswa}\n")

# Tampilkan keys(), values(), items() dan iterasi menampilkan key: value.
# keys()
print(f"Ini keys dari data_mahasiswa :{data_mahasiswa.keys()}")

# values()
print(f"Ini values dari data_mahasiswa :{data_mahasiswa.values()}")

# items()
print(f"Ini items dari data_mahasiswa :{data_mahasiswa.items()}\n")

# iterasi dengan key:value
for key, value in data_mahasiswa.items():
    print(f"{key}: {value}")
print("\n")

# Nested structure
# Buat list berisi ≥ 4 dict (mis. daftar buku: judul, penulis, tahun).
daftar_buku = [
    {"Judul": "Laskar Pelangi", "Penulis": "Andrea Hirata", "Tahun": 2005},
    {"Judul": "Bumi Manusia", "Penulis": "Pramoedya Ananta Toer", "Tahun": 1980},
    {"Judul": "Filosofi Kopi", "Penulis": "Ahmad Fauzi", "Tahun": 2009},
    {"Judul": "Bungkam Suara", "Penulis": "J.S. Khairen", "Tahun": 2025}
]

# cetak semua judul dengan loop
for i in daftar_buku:
    print(i["Judul"])
print("\n")

# Filter buku terbit ≥ tahun tertentu menggunakan list comprehension.
tahun_min = 2000
buku_modern = [b for b in daftar_buku if b["Tahun"] >= tahun_min]

for b in buku_modern:
    print(b["Judul"], "-", b["Tahun"])
print("\n")


# Comprehension dan utilitas

# List comprehension: dari daftar angka 1–20, buat list genap dan list kuadrat.
angka = list(range(1, 21))

genap = [i for i in angka if i & 2 == 0]
kuadrat = [i**2 for i in angka]

print(f"genap ={genap}")
print(f"kuadrat ={kuadrat}")

# Dict comprehension: mapping {angka: "genap"/"ganjil"} untuk 1–10.
paritas = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print(paritas)

# Set comprehension: huruf unik (lowercase) dari sebuah kalimat.
kalimat = "Belajar Python Itu Asik"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print(huruf_unik)

# Keanggotaan & pencarian sederhana
# list
buah = ["pisang", "apel", "nanas"]
print(f"Posisi array pisang :{buah.index("pisang")}")

# set
buku = {"Bungkam Suara", "Laskar Pelangi", "Filosofi Kopi"}
print(f"Cek apakah ada bungkam suara di set :{("Bungkam Suara" in buku)}")

# Set tidak bisa menyimpan index jadi kita tidak dapat menggunakan buku.index()
