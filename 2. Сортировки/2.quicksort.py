def quicksort(array):
    if(len(array) < 2):
        return array
    else:
        left = []
        right = []
        mid_element = array[len(array) // 2]
        for elem in array:
            if elem <= mid_element:
                left.append(elem)
            else:
                right.append(elem)
        return quicksort(left) + [mid_element] + quicksort(right)

array = [1, 1, 8, 3, 6, 1, 8, 90, 45, 3]
print(array)
array = quicksort(array)
print(array)
