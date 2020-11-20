white = '#ffffff'
red = '#ff0000'


def CocktailSort(arr, func):

    def Forward(low, high, arr):
        i = low
        while i < high - 1:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            func(arr, [red if x == i or x == i+1 else white for x in range(len(arr))])
            i += 1

    def Backward(low, high, arr):
        j = high
        while j > low:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            func(arr, [red if x == j or x == j - 1 else white for x in range(len(arr))])
            j -= 1

    def Sorted(arr):
        top = len(arr) - 1
        i = 0

        while i < top:
            if arr[i] > arr[i+1]:
                return False
            i += 1

        return True

    low, high = 0, len(arr) - 1

    while not Sorted(arr):
        Forward(low, high, arr)
        Backward(low, high, arr)
        low += 1
        high -= 1
    return arr


# arr = [x for x in range(100)]
# random.shuffle(arr)
# result = cocktailSort(arr)
# print(result)
