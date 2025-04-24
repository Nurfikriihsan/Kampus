# Meminta pengguna untuk memasukkan jumlah barang yang akan dibeli
N = int(input("Masukkan jumlah barang yang akan dibeli: "))

# Inisialisasi variabel total pembelian
total_pembelian = 0

# Memasukkan harga dan jumlah barang untuk setiap barang
for i in range(N):
    harga = float(input(f"Masukkan harga barang ke-{i + 1}: $"))
    jumlah = int(input(f"Masukkan jumlah barang ke-{i + 1}: "))

    # Menghitung total pembelian untuk barang ini
    total_barang = harga * jumlah

    # Menambahkan total barang ini ke total_pembelian
    total_pembelian += total_barang

# Menampilkan total pembelian
print(f"Total pembelian untuk {N} barang adalah: ${total_pembelian:.2f}")
