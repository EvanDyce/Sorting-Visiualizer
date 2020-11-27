import time


red = '#ff0000'
white = '#ffffff'


def ShellSort(arr, func, sleeptime):
    gaps = [132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        for i in range(gap, len(arr)):
            temp = arr[i]

            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
                func(arr, [red if x == j or x == j-gap else white for x in range(len(arr))])
                time.sleep(sleeptime)

            arr[j] = temp
    return arr