# Memasukkan nilai dari user
nilai = float(input("Masukkan nilai Anda: "))

# Menentukan kelulusan
if nilai >= 80:
    print("Selamat, Anda LULUS!")
elif nilai >= 75:
    print("Anda LULUS, tetapi perlu lebih baik lagi.")
else:
    print("Maaf, Anda TIDAK LULUS.")
