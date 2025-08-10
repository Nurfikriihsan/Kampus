def fibonacci(panjang):
    if panjang < 1:
        return []

    sequence = [0, 1]
    for _ in range(2, panjang):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence[:panjang]

# Input panjang deret
panjang = int(input('Masukkan panjang deret: '))

# Hasil deret Fibonacci
print(fibonacci(panjang))
