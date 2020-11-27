import time
import math

red = '#ff0000'
green = '#00b32d'
black = '#000000'
white = '#ffffff'
grey = '#a6a2a2'
purple = '#ce9eff'
light_blue = '#94afff'
light_pink = '#ffbffc'
light_yellow = '#fffebf'


def CombSort(array, func, timeSleep):
    gap = len(array)
    shrink = 1.3
    sorted = False

    while not sorted:
        start = 0
        gap = math.floor(gap/shrink)

        if gap <= 1:
            gap = 1
            sorted = True

        while start + gap < len(array):
            if array[start] > array[start+gap]:
                array[start], array[start+gap] = array[start+gap], array[start]
                sorted = False
            func(array, [red if x == start or x == start+gap else white for x in range(len(array))])
            start += 1
        time.sleep(timeSleep)
    return array
