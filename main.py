#!/usr/bin/python3

from PIL import Image, ImageDraw
from random import randint

def rectangles_cut(im_size, rect_count):
    """ Returns a list of coordinates of rectangles that subdivide an image of
    size im_size, with rectangleCount the number of rectangles in each
    dimension (X & Y axis) """
    rectangles = []

    # X and Y size of rectangles
    rect_size = \
    (
        int(im_size[0] / rect_count[0]),
        int(im_size[1] / rect_count[1])
    )

    # Construct the list of rectangles
    for i in range(0, rect_count[0]):
        for j in range(0, rect_count[1]):
            rect = [
                (i * rect_size[0], j * rect_size[1]),
                ((i + 1) * rect_size[0], j * rect_size[1]),
                ((i + 1) * rect_size[0], (j + 1) * rect_size[1]),
                (i * rect_size[0], (j + 1) * rect_size[1])
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
