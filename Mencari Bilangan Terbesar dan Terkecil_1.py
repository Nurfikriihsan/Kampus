import datetime

# User memasukkan tanggal
tahun = int(input("Masukkan tahun: "))
bulan = int(input("Masukkan bulan: "))
hari = int(input("Masukkan hari: "))

# Validasi tanggal
try:
    tanggal = datetime.date(tahun, bulan, hari)
except ValueError:
    print("Tanggal yang dimasukkan tidak valid.")
else:
    # Menentukan hari dari tanggal yang dimasukkan
    nama_hari = tanggal.strftime("%A")
    print(f"{hari:02d}/{bulan:02d}/{tahun} adalah hari {nama_hari}.")
