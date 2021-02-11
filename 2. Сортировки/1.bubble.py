def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if(array[j] > array[j + 1]):
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
    return array

array = [2, 5, 8, 3, 6, 1, 8, 90, 45, 3]
print(array)
array = bubble_sort(array)
print(array)
