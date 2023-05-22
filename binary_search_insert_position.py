def binary_search_insertion_index(data, target):
    low = 0
    high = len(data)

    while low < high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low

data = [2, 4, 6, 8, 10, 12, 14]
target = 7

insertion_index = binary_search_insertion_index(data, target)

print(f"Elemen {target} dapat disisipkan pada indeks {insertion_index} untuk menjaga daftar tetap terurut.")