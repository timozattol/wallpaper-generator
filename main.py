#!/usr/bin/python3

from PIL import Image, ImageDraw
from random import seed, randint
from polylattice import PolyLattice
from colors import palettes

def main():
    seed('42')

    im = Image.new("RGB", [1200, 800], 0)
    image_draw = ImageDraw.Draw(im)
    polylattice = PolyLattice(im.size, (12, 8))

    polylattice.initialise()
    polylattice.mutate(40)
    polylattice.gradient_colors_random_direction(
        palettes['pastel_bright'][0],
        palettes['pastel_bright'][3]
    )

    polylattice.draw(image_draw)
    im.show()

if __name__ == '__main__':
    main()
