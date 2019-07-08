# 2019 June 23 - Converted from Khan Academy
# 2019 June 24 - Visualised

import random

randomData = list()
data = list()
sampleSize = 800
dataRange = 200

for i in range(0, sampleSize):
    num = random.randint(0, dataRange)
    data.append(num)
    randomData.append(num)


def swap(array, first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp


def selectionSort():
    for i in range(0, len(data)):
        min = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min]:
                min = j
        swap(data, min, i)


selectionSort()


def check():
    status = "Sorted OK"
    errors = list()
    for i in range(0, len(data) - 1):
        if data[i] <= data[i + 1]:
            pass
        else:
            status = "Not sorted"
            errors.append(i)
    print(status)
    if len(errors) > 0:
        print(errors)


check()



from tkinter import *


canvas_width = sampleSize
canvas_height = dataRange * 2 + 20
master = Tk()
master.title("Selection Sort - Converted from Khan Academy on 2019 June 23 - Visualised on June 24")

window = Canvas(master, width = canvas_width, height = canvas_height)

window.pack()

window.create_rectangle(0, 0, canvas_width, canvas_height, fill = "light grey")

for i in range(0, sampleSize):
    window.create_line(i, canvas_height, i,
                       canvas_height - randomData[i],
                       fill = "magenta")
    window.create_line(i, canvas_height / 2, i,
                       canvas_height / 2 - data[i],
                       fill = "blue")


#window.mainloop()
#mainloop() by itself works fine
