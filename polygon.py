from random import random, randint


## Polygon class ##

class Polygon:
    """
    Represents a polygon, with vertices and a color,
    that can be drawn on a canvas.
    """

    def __init__(self, vertices, color=(0, 0, 0)):
        self.vertices = vertices
        self.color = color

    def draw(self, image_draw):
        """ Draw the polygon on the image_draw """
        image_draw.polygon([v.coordinates for v in self.vertices], self.color)

    def set_random_color(self):
        """ Set the polygon to be colored at random """
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    @property
    def center(self):
        """ Returns the coordinates of the center of the polygon """
        x, y = 0, 0

        for v in self.vertices:
            x += v.get_x()
            y += v.get_y()

        x /= len(self.vertices)
        y /= len(self.vertices)

        return (int(x), int(y))


    def __repr__(self):
        coordinates = map(lambda v: v.coordinates, self.vertices)

        string = ""

        for c in coordinates:
            string += c.__repr__()

        return "[{}]".format(string)

class Vertex:
    """
    A vertex in two dimensions. Mutations can be applied so that it randomly
    moves in the 2D world.
    """
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __repr__(self):
        return self.coordinates.__repr__()

    def get_x(self):
        return self.coordinates[0]

    def get_y(self):
        return self.coordinates[1]

    def random_mutation(self, intensity):
        """ Mutate randomly on x and y axis """

        # Mutations from -1 to +1
        mutation_x = (random() * 2) - 1
        mutation_y = (random() * 2) - 1

        # Mutations from -intensity to +intensity
        mutation_x *= intensity
        mutation_y *= intensity


        self.coordinates = \
            (
                self.coordinates[0] + mutation_x,
                self.coordinates[1] + mutation_y
            )
