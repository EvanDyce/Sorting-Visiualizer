import time

white = '#ffffff'
red = '#ff0000'


def InsertionSort(array, func, timeSleep):
    i = 1
    while i < len(array):
        j = i
        while j > 0:
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            func(array, [red if x == j else white for x in range(len(array))], 0.001)
            j -= 1
            time.sleep(timeSleep)
        i += 1
    return array
