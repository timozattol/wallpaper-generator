#!/usr/bin/python3

from PIL import Image, ImageDraw
from random import seed, randint
from polylattice import PolyLattice

def main():
    seed('42')

    im = Image.new("RGB", [1200, 800], 0)

    image_draw = ImageDraw.Draw(im)

    polylattice = PolyLattice(im.size, (12, 8))

    polylattice.initialise()

    polylattice.mutate(40)
    polylattice.gradient_colors(
        (168, 223, 32),
        (106, 32, 159),
        # Inefficient but temporary
        lambda polygon: polygon.get_center()[0] + polygon.get_center()[1]
    )
    polylattice.draw(image_draw)

    im.show()

if __name__ == '__main__':
    main()
