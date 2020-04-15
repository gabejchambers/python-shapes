import os
from tkinter import *
import re
from rectpack import newPacker


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

    packer = newPacker()

    # Add the rectangles to packing queue
    for r in rectangle_sizes:
        packer.add_rect(*r)

    packer.add_bin(*canvasSize)

    packer.pack()

    bin = packer[0]

    rtn_rects = []
    for rect in bin:
        rtn_rects.append(Rectangle(rect.height, rect.width, rect.x, rect.y))

    return rtn_rects


# reads in a file and returns a string
def readIn(fp):
    with open(fp, 'r+') as f:
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
    for dim in textin:
        rectangles.append(Rectangle(dim[0], dim[1]))

    new_rectangles = pack(rectangles, canvasParams)

    # put rectanges on canvas:
    for rect in new_rectangles:
        canvas.set_rectangle(rect)

    mainloop()

# call main():
master = Tk()
main()


