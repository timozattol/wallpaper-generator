#!/usr/bin/python3

from PIL import Image, ImageDraw
from random import randint

def rectangles_cut(imSize, rectCount):
    """ Returns a list of coordinates of rectangles that subdivide an image of
    size imSize, with rectangleCount the number of rectangles in each
    dimension (X & Y axis) """
    rectangles = []

    # X and Y size of rectangles
    rectSize = \
    (
        int(imSize[0] / rectCount[0]),
        int(imSize[1] / rectCount[1])
    )

    # Construct the list of rectangles
    for i in range(0, rectCount[0]):
        for j in range(0, rectCount[1]):
            rect = [
                (i * rectSize[0], j * rectSize[1]),
                ((i + 1) * rectSize[0], j * rectSize[1]),
                ((i + 1) * rectSize[0], (j + 1) * rectSize[1]),
                (i * rectSize[0], (j + 1) * rectSize[1])
            ]

            rectangles.append(rect)

    return rectangles

def main():
    im = Image.new("RGB", [1600, 900], 0)

    rectangles = rectangles_cut(im.size, (8, 8))

    draw = ImageDraw.Draw(im)

    for rect in rectangles:
        draw.polygon(rect, fill=(randint(0, 255), randint(0, 255), randint(0, 255)))

    im.show()

if __name__ == '__main__':
    main()
