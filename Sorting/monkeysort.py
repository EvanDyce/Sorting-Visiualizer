import random
import time


white = '#ffffff'

correct_list = []


def shuffler(array, func, sleeptime):
    global correct_list

    for i in range(len(array)-1, 0, -1):
        if i+1 == array[i]:
            if i not in correct_list:
                correct_list.append(i)
            continue

        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]
        func(array, [white for x in range(len(array))])
        time.sleep(sleeptime)
    return array


def MonkeySort(array, func, sleeptime):
    array = shuffler(array, func, sleeptime)
    # func(array, [white for x in range(len(array))])

    return array


