#!/usr/bin/python3

from os import path, makedirs
from math import ceil
import subprocess
from PIL import Image, ImageDraw
from random import sample
from polylattice import PolyLattice
from colors import palettes

def main():

    ## Configurations ##
    palette = 'pastel_forest'
    mutation_intensity = 30

    # Polygons have a fixed size in px. Higher resolution = more polygons
    poly_sizes = (120, 100)


    ## Paths ##
    file_path = path.realpath(__file__)
    file_dir = file_path.rstrip("/main.py")

    # Create renders/ folder if necessary
    render_folder = file_dir + "/renders"
    makedirs(render_folder, exist_ok=True)

    render_file = render_folder + "/wallpaper.jpg"

    # Get resolution dynamically
    cmd1 = ['xrandr']
    cmd2 = ['grep', '*']

    process = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
    process2 = subprocess.Popen(cmd2, stdin=process.stdout, stdout=subprocess.PIPE)
    process.stdout.close()

    binary_res, _ = process2.communicate()
    binary_res = binary_res.split()[0]
    resolution = binary_res.decode("utf-8").split('x')

    width = int(resolution[0])
    height = int(resolution[1])
    screen_size = (width, height)

    # Create an image of the size of the screen
    im = Image.new("RGB", screen_size, 0)
    image_draw = ImageDraw.Draw(im)

    # Initialise a PolyLattice
    poly_count_x = (screen_size[0] / poly_sizes[0])
    poly_count_y = (screen_size[1] / poly_sizes[1])

    # Last polygons might be partly overflowing the image
    polylattice = PolyLattice(
        im.size,
        (ceil(poly_count_x), ceil(poly_count_y)),
        poly_sizes)
    polylattice.initialise(separate_in_triangles=True)

    # Choose two colors from the palette
    colors = sample(palettes[palette], 2)

    # Mutate PolyLattice and apply random gradient of colors
    polylattice.mutate(mutation_intensity)
    polylattice.gradient_colors_random_direction(colors[0], colors[1])

    # Draw the polylattice on the image
    polylattice.draw(image_draw)

    # Delete eventual previous renders
    subprocess.call(["rm", render_file], stderr=subprocess.DEVNULL)

    # Save image in renders
    im.save(render_file)

    # Update wallpaper
    subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "".join(["file://", render_file])])

if __name__ == '__main__':
    main()
