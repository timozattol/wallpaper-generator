#!/usr/bin/python3

from PIL import Image, ImageDraw
from random import randint
from polylattice import PolyLattice

def main():
    im = Image.new("RGB", [1200, 800], 0)

    image_draw = ImageDraw.Draw(im)

    polylattice = PolyLattice(im.size, (12, 8))

    polylattice.initialise()

    #polylattice.debug_print()

    polylattice.mutate(40)
    polylattice.gradient_colors((255, 0, 0), (0, 255, 255))
    polylattice.draw(image_draw)

    im.show()

if __name__ == '__main__':
    main()
