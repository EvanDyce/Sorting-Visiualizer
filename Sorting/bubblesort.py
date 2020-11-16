from time import sleep


def BubbleSort(arr, func, sleepTime):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                func(arr, ['green' if x == j or x == j +1 else 'red' for x in range(len(arr))])
                sleep(sleepTime)

