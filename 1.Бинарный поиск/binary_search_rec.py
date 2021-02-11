def binary_search_rec(value, array, low, high):
    mid = low + (high - low) // 2
    if array[mid] == value:
        return mid
    elif array[mid] < value:
        return binary_search_rec(value, array, mid + 1, high)
    else:
        return binary_search_rec(value, array, low, mid - 1)
    
array = [1, 3, 4, 5, 6, 7, 15, 156, 189, 156]
print(binary_search_rec(4, array, 0, len(array) - 1))
