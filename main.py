#!/usr/bin/python3

from PIL import Image, ImageDraw
from random import seed, randint, sample
from polylattice import PolyLattice
from colors import palettes
from os import getcwd

import subprocess

def main():
    # Set seed to control randomness
    # seed('42')

    # Choose two colors from the palette
    colors = sample(palettes['pastel_forest'], 2)

    # Create an image of the size of the screen
    im = Image.new("RGB", [1600, 900], 0)
    image_draw = ImageDraw.Draw(im)

    # Initialise a PolyLattice
    polylattice = PolyLattice(im.size, (16, 9))
    polylattice.initialise()

    # Mutate PolyLattice and apply random gradient of colors
    polylattice.mutate(40)
    polylattice.gradient_colors_random_direction(colors[0], colors[1])

    # Draw the polylattice on the image
    polylattice.draw(image_draw)

    # Delete eventual previous renders
    subprocess.call(["rm", "renders/wallpaper.jpg"], stderr=subprocess.DEVNULL)

    # Save image in renders
    im.save("renders/wallpaper.jpg")

    # Update wallpaper
    wd = getcwd()
    subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "file://" + wd + "/renders/wallpaper.jpg"])

if __name__ == '__main__':
    main()
