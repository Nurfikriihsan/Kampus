def aturan_karyawan(gaji, berkeluarga, punya_rumah_makan):
    umr = 3000000  # Ganti dengan nilai UMR yang berlaku di wilayah Anda

    if gaji > umr and berkeluarga:
        print("Karyawan wajib ikutan asuransi dan menabung untuk pensiun.")
    else:
        print("Karyawan tidak perlu ikutan asuransi.")

    if punya_rumah_makan:
        print("Karyawan wajib bayar pajak usaha.")
    else:
        print("Karyawan tidak wajib bayar pajak usaha.")

# Meminta input dari pengguna
gaji = float(input("Masukkan gaji karyawan: "))
berkeluarga = input("Apakah karyawan berkeluarga? (ya/tidak): ").lower() == 'ya'
punya_rumah_makan = input("Apakah karyawan memiliki rumah makan? (ya/tidak): ").lower() == 'ya'

# Memanggil fungsi aturan_karyawan dengan input dari pengguna
aturan_karyawan(gaji, berkeluarga, punya_rumah_makan)
