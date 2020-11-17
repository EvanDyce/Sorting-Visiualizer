from tkinter import *
# from tkinter.ttk import Scale
import random
from Sorting.bubblesort import BubbleSort
from Sorting.selectionsort import SelectionSort
import time

algoList, data, bars = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort'], [], []

red = '#ff0000'
green = '#00b32d'
black = '#000000'
white = '#ffffff'
grey = '#a6a2a2'


def drawData(array, colors, sleep):
    global bars

    graph.delete('all')
    gwidth = 1870
    gheight = 900
    bar_width = gwidth / len(array)
    coefficient = (gheight - 2) / max(array)
    counter = 0

    for num in array:
        x1 = counter * bar_width
        y1 = gheight - num * coefficient
        x2 = x1 + bar_width
        y2 = gheight
        bar = graph.create_rectangle(x1, y1, x2, y2, fill=colors[counter])
        bars.append(bar)
        counter += 1
    time.sleep(sleep)

    root.update_idletasks()


# generate function to be called
# passes return to drawData and it displays it
def Generate(max_value):
    global data
    data = []
    for i in range(1, int(max_value) + 1):
        data.append(i)

    drawData(data, ['white' for x in range(len(data))], 0)


def shuffle():
    global data
    random.shuffle(data)
    drawData(data, ['white' for x in range(len(data))], 0)


def Sorted():
    global data
    colors = [white for x in range(len(data))]
    i = 0
    while i < len(data):
        colors[i] = green
        drawData(data, colors, 0.0001)
        i += 1


def startBubble():
    global data
    BubbleSort(data, drawData, sleepTimer.get())
    Sorted()


def startSelection():
    global data
    SelectionSort(data, drawData, sleepTimer.get())
    Sorted()


# Creating the main window
root = Tk()
root.geometry('1920x1080')
root.title('Sorting Algorithms Visualized')

# adding upper frame
upper = Frame(master=root, bg=red, width=1920, height=950)
upper.grid(row=0, column=0)

# adding graph to the upper frame
graph = Canvas(upper, width=1870, height=900, bg=black)
graph.place(relx=0.5, rely=0.5, anchor=CENTER)

# adding lower frame
lower = Frame(master=root, bg=black, width=1920, height=950)
lower.grid(row=1, column=0)
lower.grid_propagate(False)

# adding buttons on lower frame
Button(lower, text='Shuffle Array', height=4, width=25, command=shuffle).grid(row=0, column=2, padx=9, pady=20)
Button(lower, text='Bubble Sort', height=4, width=25, command=startBubble).grid(row=0, column=3, padx=9, pady=20)
Button(lower, text='Selection Sort', height=4, width=25, command=startSelection).grid(row=0, column=4, padx=9,
                                                                                      pady=20)
Button(lower, text='Insertion Sort', height=4, width=25).grid(row=0, column=5, padx=9, pady=20)
Button(lower, text='algo', height=4, width=25).grid(row=0, column=6, padx=9, pady=20)
Button(lower, text='lgo', height=4, width=25).grid(row=0, column=7, padx=9, pady=20)
Button(lower, text='algo', height=4, width=25).grid(row=0, column=8, padx=9, pady=20)

# adding slider for array size and for sleepTime
slider = Scale(lower, from_=10, to=200, orient=HORIZONTAL, label='Size of Array', length=250, command=Generate)
slider.grid(row=0, column=0, padx=9, pady=40)
sleepTimer = Scale(lower, from_=0.00, to=0.10, orient=HORIZONTAL, label='Choose Speed of Sort', length=250,
                   resolution=0.01, tickinterval=0.01, showvalue=0)
sleepTimer.grid(row=0, column=1, padx=9, pady=9)

Generate(10)

root.mainloop()
