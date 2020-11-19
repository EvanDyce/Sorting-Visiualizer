import random

white = '#ffffff'
green = '#00b32d'


correct_list = []


def shuffler(array):
    global correct_list

    for i in range(len(array)-1, 0, -1):
        print(i)
        if i+1 == array[i]:
            if i not in correct_list:
                correct_list.append(i)
            continue

        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]
    return array


def MonkeySort(array, func):
    array = shuffler(array)
    func(array, [white for x in range(len(array))])

    return array


