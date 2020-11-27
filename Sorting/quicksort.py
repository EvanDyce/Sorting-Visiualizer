white = '#ffffff'
red = '#ff0000'


def partition(data, head, tail, drawData):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))


    #swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))

    data[border], data[tail] = data[tail], data[border]

    return border


def QuickSort(data, head, tail, drawData):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData)

        #LEFT PARTITION
        QuickSort(data, head, partitionIdx-1, drawData)

        #RIGHT PARTITION
        QuickSort(data, partitionIdx+1, tail, drawData)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        # if i >= head and i <= tail:
        #     colorArray.append(white)
        # else:
        #     colorArray.append('white')
        colorArray.append(white)

        if i == tail:
            colorArray[i] = red
        elif i == border:
            colorArray[i] = red
        elif i == currIdx:
            colorArray[i] = red

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray