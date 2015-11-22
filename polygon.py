from random import random, randint

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
        image_draw.polygon(self.__vertices_to_list(), self.color)

    def set_random_color(self):
        """ Set the polygon to be colored at random """
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def __repr__(self):
        coordinates = map(lambda v: v.coordinates, self.vertices)

        string = ""

        for c in coordinates:
            string += c.__repr__()

        return "[{}]".format(string)

    def __vertices_to_list(self):
        """
        Extracts coordinates of vertices, so that they can be accepted
        by the draw method imagedraw.polygon()
        """
        vertices_list = []

        for v in self.vertices:
            vertices_list.append(v.coordinates)

        return vertices_list

class Vertex:
    """
    A vertex in two dimensions. Mutations can be applied so that it randomly
    moves in the 2D world.
    """
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __hash__(self):
        self.coordinates.hash()

    def __repr__(self):
        return self.coordinates.__repr__()

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
