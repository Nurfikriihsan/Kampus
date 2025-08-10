# Fungsi pencocokan string
def string_matching(text, pattern):
    # Panjang teks dan panjang pola
    n = len(text)
    m = len(pattern)
    result = []
    
    # Perulangan dari awal teks sampai posisi terakhir
    for i in range(n - m + 1):
        match = True  
        
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            result.append(i)

    return result

if __name__ == "__main__":
    # Teks dan pola yang ingin dicocokkan
    text = "algoritma string matching adalah bagian penting dalam pemrosesan teks"
    pattern = "string"
    
    # Fungsi pencocokan
    matches = string_matching(text, pattern)
    
    # Hasil
    if matches:
        print(f"Pattern '{pattern}' ditemukan pada indeks: {matches}")
    else:
        print(f"Pattern '{pattern}' tidak ditemukan dalam teks.")
