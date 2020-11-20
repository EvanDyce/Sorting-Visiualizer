red = '#ff0000'
green = '#00b32d'
black = '#000000'
white = '#ffffff'
grey = '#a6a2a2'
purple = '#ce9eff'
light_blue = '#94afff'
light_pink = '#ffbffc'
light_yellow = '#fffebf'


def heapify(arr, n, i, func):
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
        heapify(arr, n, largest, func)


def HeapSort(arr, func):
    n = len(arr)

    for i in range(n-1, -1, -1):
        heapify(arr, n, i, func)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, func)
