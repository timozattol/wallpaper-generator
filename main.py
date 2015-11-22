#!/usr/bin/python3

from PIL import Image, ImageDraw
from random import randint
from polylattice import PolyLattice

def main():
    im = Image.new("RGB", [1600, 900], 0)

    image_draw = ImageDraw.Draw(im)

    polylattice = PolyLattice(im.size, (12, 7))

    polylattice.initialise()

    #polylattice.debug_print()

    polylattice.mutate(40)
    polylattice.randomise_colors()
    polylattice.draw(image_draw)

    im.show()

if __name__ == '__main__':
    main()
