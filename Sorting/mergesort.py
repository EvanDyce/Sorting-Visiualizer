red = '#ff0000'
green = '#00b32d'
black = '#000000'
white = '#ffffff'


import time

def MergeSort(data, drawData, timeTick):
    merge_sort_alg(data,0, len(data)-1, drawData, timeTick)


def merge_sort_alg(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick)
        merge_sort_alg(data, middle+1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1: right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawData(data, [white for x in range(len(data))])
    time.sleep(timeTick)


def getColorArray(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append(red)
            else:
                colorArray.append(red)
        else:
            colorArray.append("white")

    return colorArray


# def MergeSort(data, func):
#     merge_algo(data, 0, len(data)-1, func)
#
#
# def merge_algo(data, left, right, func):
#     if left < right:
#         middle = (left+right)//2
#         merge_algo(data, left, middle, func)
#         merge_algo(data, middle+1, right, func)
#         merge(data, left, middle, right, func)
#
#
# def merge(data, left, middle, right, func):
#
#     func(data, getColorArray(len(data), left, middle, right))
#
#     leftPart = data[left:middle+1]
#     rightPart = data[middle+1: right+1]
#
#     leftIndex, rightIndex = 0, 0
#
#     for dataIndex in range(left, right):
#
#         if leftIndex < len(leftPart) and rightIndex < len(rightPart):
#             if leftPart[leftIndex] <= rightPart[rightIndex]:
#                 data[dataIndex] = leftPart[leftIndex]
#                 leftIndex += 1
#             else:
#                 data[dataIndex] = rightPart[rightIndex]
#                 rightIndex += 1
#
#         elif leftIndex < len(leftPart):
#             data[dataIndex] = leftPart[leftIndex]
#             leftIndex += 1
#
#         else:
#             data[dataIndex] = rightPart[rightIndex]
#             rightIndex += 1
#
#     func(data, [green if left <= x <= right else white for x in range(len(data))])
#
#
# def getColorArray(length, left, middle, right):
#     colorArray = []
#
#     for i in range(length):
#         if i >= left and i <= right:
#             if i <= middle:
#                 colorArray.append(red)
#             else:
#                 colorArray.append(black)
#         else:
#             colorArray.append(green)
#
#     return colorArray