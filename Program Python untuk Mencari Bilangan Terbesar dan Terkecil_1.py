import datetime

# Minta pengguna untuk memasukkan tanggal
tahun = int(input("Masukkan tahun (contoh: 2023): "))
bulan = int(input("Masukkan bulan (1-12): "))
hari = int(input("Masukkan hari (1-31): "))

# Validasi tanggal
try:
    tanggal = datetime.date(tahun, bulan, hari)
except ValueError:
    print("Tanggal yang dimasukkan tidak valid.")
else:
    # Menentukan hari dari tanggal yang dimasukkan
    nama_hari = tanggal.strftime("%A")
    print(f"{hari:02d}/{bulan:02d}/{tahun} adalah hari {nama_hari}.")
