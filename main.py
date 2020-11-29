import random
from tkinter import *
from tkinter import font

from Sorting.bubblesort import BubbleSort
from Sorting.cocktailsort import CocktailSort
from Sorting.combsort import CombSort
from Sorting.heapsort import HeapSort
from Sorting.insertionsort import InsertionSort
from Sorting.mergesort import MergeSort
from Sorting.monkeysort import MonkeySort
from Sorting.quicksort import QuickSort
from Sorting.selectionsort import SelectionSort
from Sorting.shellsort import ShellSort

algoList = ['Monkey Sort', 'Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Cocktail Sort', 'Comb Sort', 'Shell Sort', 'Heap Sort', 'Quick Sort', 'Merge Sort']
speedList = ['Noma']
bars, data = [], [i for i in range(1, 11)]


red = '#ff0000'
green = '#00b32d'
black = '#000000'
white = '#ffffff'
grey = '#a6a2a2'


class Application(Tk):
    def __init__(self, parent) -> None:
        Tk.__init__(self)
        self.parent = parent
        self.geometry('1920x1080')
        self.title('Sorting Algorithms')
        self.upper = Upper(self)
        self.lower = Lower(self)


class Lower(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, master=parent, bg=black, width=1920, height=950)
        # self.graph = graph
        self.parent = parent
        self.grid(row=1, column=0)
        self.grid_propagate(False)
        self.populate()


    def populate(self):
        # sliders
        self.size_slider = Scale(self, from_=10, to=250, orient='horizontal', label='Size of Array', length=250, command=self.parent.upper.graph.generate_data)
        self.size_slider.grid(row=0, column=0, padx=70, pady=40)
        self.time_slider = Scale(self, from_=1, to=10, orient=HORIZONTAL, label='Sorting Speed', length=250, resolution=1, tickinterval=1, showvalue=0)
        self.time_slider.grid(row=0, column=1, padx=70)

        # buttons
        self.shuffle_button = Button(self, text='Shuffle Array', height=5, width=30, command=self.parent.upper.graph.shuffle)
        self.shuffle_button.grid(row=0, column=3, padx=70)
        self.sort_button = Button(self, text='Sort', height=5, width=30, command=self.parent.upper.graph.begin_sort)
        self.sort_button.grid(row=0, column=5, padx=70)

        # dropdown
        font.Font(family='Helvetica', name='hel')
        self.variable = StringVar(self)
        self.variable.set('Select an Algorithm')
        self.dropdown = OptionMenu(self, self.variable, *algoList)
        self.dropdown.configure(height=1, width=20, font='hel')
        self.dropdown['menu'].config(font='hel')
        self.dropdown.grid(row=0, column=4, padx=70)


    def get_variable(self):
        return self.variable.get()

    def get_time_slider(self):
        return self.time_slider.get()


class Upper(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, master=parent, bg=red, width=1920, height=950)
        self.parent = parent
        self.grid(row=0, column=0)
        self.grid_propagate(False)
        self.graph = Graph(self)

    def add_graph(self, width, height, bg):
        self.graph = Canvas(self, width=width, height=height, bg=bg)
        self.graph.place(relx=0.5, rely=0.5, anchor=CENTER)
        

class Graph(Canvas):
    def __init__(self, parent) -> None:
        Canvas.__init__(self, master=parent, bg=black, width=1870, height=900)
        self.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.parent = parent
        self.width = 1870
        self.height = 900
        self.draw_data(data, [white for x in range(len(data))])


    def generate_data(self, max_value):
        global data

        data = []

        for i in range(1, int(max_value)+1):
            data.append(i)

        self.draw_data(data, [white for x in range(len(data))])


    def shuffle(self):
        global data

        random.shuffle(data)
        self.draw_data(data, [white for x in range(len(data))])


    def draw_data(self, array, colors):
        global bars

        self.delete('all')
        bar_width = self.width / len(array)
        coefficient = (self.height - 2) / max(array)

        for counter, num in enumerate(array):
            x1 = counter * bar_width
            x2 = x1 + bar_width
            y1 = self.height - num * coefficient
            y2 = self.height
            bar = self.create_rectangle(x1, y1, x2, y2, fill=colors[counter])
            bars.append(bar)

        self.parent.parent.update_idletasks()
    

    def begin_sort(self):
        global data

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

        if self.parent.parent.lower.get_variable() == 'Monkey Sort':
            monke = []
            while monke != sorted(data):
                monke = function_dict[self.parent.parent.lower.get_variable()](monke, [white for x in range(len(monke))])

        elif self.parent.parent.lower.get_variable() == 'Quick Sort':
            QuickSort(data, 0, len(data)-1, self.draw_data)

        else:
            function_dict[self.parent.parent.lower.get_variable()](data, self.draw_data, (self.parent.parent.lower.time_slider.get()/10-0.1))

        self.is_sorted()

    def is_sorted(self):
        global data
        
        colors = [white for x in range(len(data))]
        i = 0 

        if len(data) % 5 == 0:
            while i < len(data):
                colors[i], colors[i+1], colors[i+2], colors[i+3], colors[i+4] = green, green,green,green,green,
                self.draw_data(data, colors)
                i += 5

        elif len(data) % 4 == 0:
            while i < len(data):
                colors[i], colors[i+1], colors[i+2], colors[i+3] = green,green,green,green,
                self.draw_data(data, colors)
                i += 4

        elif len(data) % 3 == 0:
            while i < len(data):
                colors[i], colors[i+1], colors[i+2] = green,green,green,
                self.draw_data(data, colors)
                i += 3

        elif len(data) % 2 == 0:
            while i < len(data):
                colors[i], colors[i+1] = green,green,
                self.draw_data(data, colors)
                i += 2

        else:
            while i < len(data):
                colors[i] = green
                self.draw_data(data, colors)
                i += 1


if __name__ == "__main__":
    app = Application(None)
    app.mainloop()

