from time import sleep
import random


red = '#ff0000'
green = '#00b32d'
black = '#000000'
white = '#ffffff'
grey = '#a6a2a2'
purple = '#ce9eff'
light_blue = '#94afff'
light_pink = '#ffbffc'
light_yellow = '#fffebf'


def SelectionSort(arr, func, timesleep):
    i = 0
    while i < len(arr)-1:
        current = arr[i]
        j = i+1
        while j < len(arr):
            if arr[j] < current:
                current = arr[j]
                arr[i], arr[j] = arr[j], arr[i]
            func(arr, [red if x == j or x == i else white for x in range(len(arr))])
            sleep(timesleep)
            j += 1
        i += 1



