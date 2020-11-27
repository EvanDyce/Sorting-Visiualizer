from time import sleep


red = '#ff0000'
green = '#00b32d'
black = '#000000'
white = '#ffffff'
grey = '#a6a2a2'
purple = '#ce9eff'
light_blue = '#94afff'
light_pink = '#ffbffc'
light_yellow = '#fffebf'


def BubbleSort(arr, func, sleepTime):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                func(arr, [red if x == j or x == j + 1 else white for x in range(len(arr))])
                sleep(sleepTime)



def defocus(event):
    event.dropdown.lower.focus_set()