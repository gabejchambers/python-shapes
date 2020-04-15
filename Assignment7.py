import os
from tkinter import *
import re
import rpack

# 1) create custom canvas class:

'''
class example:

# Class for Computer Science Student
class Dog:

    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed):

        # Instance Variable
        self.breed = breed

    # Adds an instance variable
    def setColor(self, color):
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color

# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())
'''


class CustomCanvas:

    def __init__(self, height, width):
        self.height = height  # int
        self.width = width  # int
        self.c = Canvas(master, height=height, width=width)
        self.c.pack()

    def set_rectangle(self, rect):
        self.c.create_rectangle(rect.x, rect.y, rect.x + rect.width, rect.y + rect.height, fill="#00f")


class Rectangle:

    def __init__(self, height, width, x=0, y=0):
        self.height = height  # int
        self.width = width  # int
        self.x = x  # int
        self.y = y  # int


# pack will take the given list of rectangles and determine a location
# for each rectangle so that each rectangle does not overlap another and each
# rectangle exists within the given canvas size.

# Pack will then return a list of placed Rectangle objects. Each given
# rectangle must be included in the returned list.
def pack(allRect, canvasSize):
    # where allRect is a list of Rectangle obejcts
    # canvasSize os a tuple containing a canvas (height, width)
    rectangle_sizes = []
    for rect in allRect:
        rectangle_sizes.append((rect.width, rect.height))
    print(rectangle_sizes)  # testing
    rectangle_positions = rpack.pack(rectangle_sizes)
    print(rectangle_positions)

    rtn_rects = []
    for rectIndex in range(len(allRect)):
        rtn_rects.append(
            Rectangle(allRect[rectIndex].height, allRect[rectIndex].width, rectangle_positions[rectIndex][0],
                      rectangle_positions[rectIndex][1]))

    return rtn_rects


# reads in a file and returns a string
def readIn(fp):
    pn = re.search(r'(.*?\\)([^\\]*?)$', fp)
    path = pn.group(1)
    name = pn.group(2)
    os.chdir(path)
    with open(name, 'r+') as f:
        lines = []
        for line in f:
            lines.append(
                (int(re.search(r'(.*),.*', line.strip()).group(1)), int(re.search(r'.*,(.*)', line.strip()).group(1))))
        return lines


def main():
    pythonFileName = sys.argv.pop(0)
    fpath = sys.argv.pop(0)
    textin = readIn(fpath)

    canvasParams = textin.pop(0)
    canvas = CustomCanvas(canvasParams[0], canvasParams[1])

    # create initial rectangle objects at origin
    rectangles = []
    rectangle_sizes = rpack.pack(textin)
    for dim in textin:
        rectangles.append(Rectangle(dim[0], dim[1]))

    new_rectangles = pack(rectangles, canvasParams)

    # put rectanges on canvas:
    for rect in new_rectangles:
        canvas.set_rectangle(rect)

    #####TESTING##########
    # print(canvasParams)
    # print(rectangle_sizes)  # testing
    # for rect in rectangles:
    #    print(rect.width, rect.height)
    #####END TESTING######


# call main():
master = Tk()
main()
mainloop()

#####TESTING######
# myCanvas = CustomCanvas(150, 1000)
# print()
###END TESTING####
