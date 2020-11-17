from time import sleep


red = '#ff0000'
green = '#00b32d'
black = '#000000'
white = '#ffffff'


def BubbleSort(arr, func, sleepTime):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                func(arr, [red if x == j or x == j + 1 else white for x in range(len(arr))], 0)
                sleep(sleepTime)

