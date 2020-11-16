from time import sleep
import random

def SelectionSort(arr, func, timesleep):
    i = 0
    while i < len(arr)-1:
        current = arr[i]
        j = i+1
        while j < len(arr):
            if arr[j] < current:
                current = arr[j]
                arr[i], arr[j] = arr[j], arr[i]
            func(arr, ['green' if x == j or x == i else 'red' for x in range(len(arr))])
            sleep(timesleep)
            j += 1
        i += 1



