import time

red = '#ff0000'
white = '#ffffff'


def heapify(arr, n, i, func, sleeptime):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        func(arr, [red if x == arr[i] or x == arr[largest] else white for x in range(len(arr))])
        time.sleep(sleeptime)
        heapify(arr, n, largest, func, sleeptime)


def HeapSort(arr, func, sleeptime):
    n = len(arr)

    for i in range(n-1, -1, -1):
        heapify(arr, n, i, func, sleeptime)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, func, sleeptime)
