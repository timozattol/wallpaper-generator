#!/usr/bin/python3

from PIL import Image, ImageDraw
from random import seed, randint, sample
from polylattice import PolyLattice
from colors import palettes
from os import path
import subprocess

def main():
    ## Configurations ##
    palette = 'pastel_forest'

    # Get resolution dynamically
    cmd1 = ['xrandr']
    cmd2 = ['grep', '*']

    process = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
    process2 = subprocess.Popen(cmd2, stdin=process.stdout, stdout=subprocess.PIPE)
    process.stdout.close()

    binary_res, ununsed = process2.communicate()
    binary_res = binary_res.split()[0]
    resolution = binary_res.decode("utf-8").split('x')

    screen_size = (int(resolution[0]), int(resolution[1]))

    chunk_size = (100, 100) # screen_size / chunk_size have to be integer
    mutation_intensity = 30

    ## Paths ##
    file_path = path.realpath(__file__)
    file_dir = file_path.rstrip("/main.py")
    render_path = file_dir + "/renders/wallpaper.jpg"

    # Set seed to control randomness
    # seed('42')

    # Create an image of the size of the screen
    im = Image.new("RGB", screen_size, 0)
    image_draw = ImageDraw.Draw(im)

    # Initialise a PolyLattice
    poly_size_x = int(screen_size[0] / chunk_size[0])
    poly_size_y = int(screen_size[1] / chunk_size[1])
    polylattice = PolyLattice(im.size, (poly_size_x, poly_size_y))
    polylattice.initialise(separate_in_triangles=True)

    # Choose two colors from the palette
    colors = sample(palettes[palette], 2)

    # Mutate PolyLattice and apply random gradient of colors
    polylattice.mutate(mutation_intensity)
    polylattice.gradient_colors_random_direction(colors[0], colors[1])

    # Draw the polylattice on the image
    polylattice.draw(image_draw)

    # Delete eventual previous renders
    subprocess.call(["rm", render_path], stderr=subprocess.DEVNULL)

    # Save image in renders
    im.save(render_path)

    # Update wallpaper
    subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "".join(["file://", render_path])])

if __name__ == '__main__':
    main()
