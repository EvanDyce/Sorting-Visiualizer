
red = '#ff0000'
green = '#00b32d'
black = '#000000'
white = '#ffffff'
grey = '#a6a2a2'
purple = '#ce9eff'
light_blue = '#94afff'
light_pink = '#ffbffc'
light_yellow = '#fffebf'


def ShellSort(arr, func):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        for i in range(gap, len(arr)):
            temp = arr[i]

            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
                func(arr, [red if x == j or x == j-gap else purple for x in range(len(arr))])

            arr[j] = temp
    return arr