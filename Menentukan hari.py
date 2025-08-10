# Memasukkan pendapatan dan biaya perusahaan
pendapatan = float(input("Masukkan total pendapatan perusahaan: $"))
biaya = float(input("Masukkan total biaya perusahaan: $"))

# Menghitung laba atau rugi
laba_rugi = pendapatan - biaya

# Menentukan apakah perusahaan menghasilkan laba atau rugi
if laba_rugi > 0:
    print(f"Perusahaan menghasilkan laba sebesar ${laba_rugi:.2f}")
elif laba_rugi < 0:
    print(f"Perusahaan mengalami rugi sebesar ${abs(laba_rugi):.2f}")
else:
    print("Perusahaan tidak menghasilkan laba maupun rugi.")
