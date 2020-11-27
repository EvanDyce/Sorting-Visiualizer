import time

red = '#ff0000'
green = '#00b32d'
black = '#000000'
white = '#ffffff'
grey = '#a6a2a2'
purple = '#ce9eff'
light_blue = '#94afff'
light_pink = '#ffbffc'
light_yellow = '#fffebf'


def InsertionSort(array, func, timeSleep):
    i = 1
    while i < len(array):
        j = i
        while j > 0:
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            func(array, [red if x == j else white for x in range(len(array))])
            j -= 1
            time.sleep(timeSleep)
        i += 1
    return array
