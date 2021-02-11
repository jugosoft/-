#-*- coding:utf-8 -*-
def binary_search(array, elem):
    low = 0
    high = len(array) - 1
    #counter = 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = array[mid]
        if guess == elem:
            #print(mid, "iterations: ", counter)
            return mid
        if guess >= elem:
            high = mid - 1
        else:
            low = mid + 1
        #counter = counter + 1
    return None

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

binary_search(array, 3)

