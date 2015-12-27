# wallpaper-generator

A simple wallpaper generator in python, to have fun with graphics and python.

Inspired by [this kind of wallpaper](http://imgur.com/m5tjwjp).

## Compatibility

You need python3 and the requirements that are in `requirements.txt` (basically [`Pillow`](https://pypi.python.org/pypi/Pillow/3.0.0)). Unfortunately, the commands I use to create the files might only work on UNIX systems, and the command to update your desktop wallpaper works with Gnome / Unity (tested under Ubuntu 14.04).

Feel free to tweak the program to work on your system, you can even open a pull request if you want to integrate your tweaks.

## Installation

Install python3, the requirements in `requirements.txt`, and then you're good to go. Executing `main.py` will create a wallpaper in `renders/` and update your Gnome/Unity wallpaper. With `install_cron.sh`, you can even install a cron job that changes your wallpaper every 30 minutes.

## Result

Here's what it gives with colors picked from a palette, on my Ubuntu desktop. If you ask yourself, I use the wonderful [Flatabulous theme](https://github.com/anmoljagetia/Flatabulous) for icons and windows.

![Desktop](http://i.imgur.com/mKXScYB.png)

## Algorithm

The algorithm is quite simple:

* First a lattice of rectangles is created, here shown with random colors for rectangles

![Lattice](http://i.imgur.com/d2ZrDSP.png)

* Then, a random mutation (translation) is applied to the vertices of the lattice

![Lattice mutated](http://i.imgur.com/lfq9DjK.png)

* Then, a gradient of colors can be applied to the polygons

![Lattice gradient](http://i.imgur.com/U76k1Hs.png)

* Different angles can be used for the gradient

![Lattice gradient angle](http://i.imgur.com/GEPyVcp.png)

## Examples

Here's the effect, when colors are picked from a palette of 5 colors at random, angle is chosen at random and mutations are random:

![Wallpaper1](http://i.imgur.com/91kURkf.jpg)
![Wallpaper2](http://i.imgur.com/xpdL3BI.jpg)
![Wallpaper3](http://i.imgur.com/zXlmQ7P.jpg)
![Wallpaper4](http://i.imgur.com/a28sxB0.jpg)



