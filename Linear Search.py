def linear_search(arr, target):
   
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

if __name__ == "__main__":
    data = [4, 2, 7, 1, 9, 5]
    target_element = 7

    result = linear_search(data, target_element)

    if result != -1:
        print(f"Elemen ditemukan di indeks ke-{result}")
    else:
        print("Elemen tidak ditemukan dalam array")
