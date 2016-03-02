#!/usr/bin/python3

from os import path, makedirs
import subprocess
from PIL import Image, ImageDraw
from random import seed, sample
from polylattice import PolyLattice
from colors import palettes


# Possible resolution and their respective chunk size (TODO need to find better solution)
res_chunk_map = {
    (3840, 2160): (240, 135),
    (1920, 1080): (160, 90),
    (1600, 900): (100, 100),
    (1440, 900):(96, 100),
    (1360, 768): (136, 64),
    (1024, 768): (128, 96),
    (800, 600): (100, 100),
    (640, 480): (80, 60)
}

def main():
    ## Configurations ##
    palette = 'pastel_forest'
    mutation_intensity = 30

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

    # Get known chunk size if possible
    chunk_size = res_chunk_map.get((width, height), (width / 12, height / 8))

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
    subprocess.call(["rm", render_file], stderr=subprocess.DEVNULL)

    # Save image in renders
    im.save(render_file)

    # Update wallpaper
    subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "".join(["file://", render_file])])

if __name__ == '__main__':
    main()
