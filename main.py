from tkinter import *
from tkinter import font
import datetime
import random
from Sorting.bubblesort import BubbleSort
from Sorting.selectionsort import SelectionSort
from Sorting.insertionsort import InsertionSort
from Sorting.combsort import CombSort
from Sorting.monkeysort import MonkeySort
from Sorting.shellsort import ShellSort
from Sorting.heapsort import HeapSort
from Sorting.mergesort import MergeSort
from Sorting.cocktailsort import CocktailSort
from Sorting.quicksort import QuickSort


algoList = ['Monkey Sort', 'Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Cocktail Sort', 'Comb Sort', 'Shell Sort', 'Heap Sort', 'Quick Sort', 'Merge Sort']
speedList = ['Noma']
bars, data = [], []
selected_alg = ''



red = '#ff0000'
green = '#00b32d'
black = '#000000'
white = '#ffffff'
grey = '#a6a2a2'


def drawData(array, colors):
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

    root.update_idletasks()


# generate function to be called
# passes return to drawData and it displays it
def Generate(max_value):
    global data
    data = []
    for i in range(1, int(max_value) + 1):
        data.append(i)

    drawData(data, [white for x in range(len(data))])


def shuffle():
    global data
    random.shuffle(data)
    drawData(data, [white for x in range(len(data))])


def Sorted():
    global data

    is_sorted = True

    colors = [white for x in range(len(data))]
    i = 0

    if len(data) % 5 == 0:
        while i < len(data):
            colors[i], colors[i+1], colors[i+2], colors[i+3], colors[i+4] = green, green,green,green,green,
            drawData(data, colors)
            i += 5

    elif len(data) % 4 == 0:
        while i < len(data):
            colors[i], colors[i+1], colors[i+2], colors[i+3] = green,green,green,green,
            drawData(data, colors)
            i += 4

    elif len(data) % 3 == 0:
        while i < len(data):
            colors[i], colors[i+1], colors[i+2] = green,green,green,
            drawData(data, colors)
            i += 3

    elif len(data) % 2 == 0:
        while i < len(data):
            colors[i], colors[i+1] = green,green,
            drawData(data, colors)
            i += 2

    else:
        while i < len(data):
            colors[i] = green
            drawData(data, colors)
            i += 1


def begin_sort():
    global data
    global first_sum

    full = datetime.datetime.now()
    date_minute = full.minute
    date_second = full.second
    first_sum = date_minute*60 + date_second


    function_dict = {
        # select an algorithm error message in the window
        'Monkey Sort': MonkeySort,
        'Bubble Sort': BubbleSort,
        'Selection Sort': SelectionSort,
        'Insertion Sort': InsertionSort,
        'Cocktail Sort': CocktailSort,
        'Comb Sort': CombSort,
        'Shell Sort': ShellSort,
        'Heap Sort': HeapSort,
        'Quick Sort': QuickSort,
        'Merge Sort': MergeSort
    }

    if variable.get() == 'Monkey Sort':
        monke = []
        while monke != sorted(data):
            monke = function_dict[variable.get()](data, drawData, sleepTimer.get())
            drawData(monke, [white for x in range(len(monke))])

    elif variable.get() == 'Quick Sort':
        QuickSort(data, 0, len(data)-1, drawData)

    else:
        function_dict[variable.get()](data, drawData, sleepTimer.get())

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

fun = font.Font(family='Helvetica', name='hel15')

# adding combobox and label
variable = StringVar(lower)
variable.set("Select an Algorithm")
dropdown = OptionMenu(lower, variable, *algoList)
dropdown.configure(height=1, width=20, font='hel15')
dropdown['menu'].config(font='hel15')
dropdown.grid(row=0, column=4, padx=30)

# adding sort button
Button(lower, text='Shuffle Array', height=4, width=25, command=shuffle).grid(row=0, column=3, padx=30)
Button(lower, text='Sort', height=4, width=25, command=begin_sort).grid(row=0, column=5, padx=30)


# adding slider for array size and for sleepTime
slider = Scale(lower, from_=10, to=250, orient=HORIZONTAL, label='Size of Array', length=250, command=Generate)
slider.grid(row=0, column=0, padx=30, pady=40)
sleepTimer = Scale(lower, from_=0.00, to=0.10, orient=HORIZONTAL, label='Choose Speed of Sort', length=250, resolution=0.01, tickinterval=0.01, showvalue=0)
sleepTimer.grid(row=0, column=1, padx=30, pady=9)


Generate(10)

root.mainloop()
