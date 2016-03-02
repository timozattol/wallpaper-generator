from polygon import Vertex, Polygon
from random import random
from math import pi, sin, cos

class PolyLattice:
    """
    A lattice of polygons, with polygon_counts describing the number of polygons
    on each axis.
    """

    def __init__(self, image_size, polygon_counts, polygon_sizes):
        self.image_size = image_size
        self.polygon_counts = polygon_counts
        self.polygon_sizes = polygon_sizes

        # The polygons list.
        self.polygons = []

        # The vertices matrix, used by the polygons
        self.vertices = {}

    def draw(self, image_draw):
        """ Draw the polygons of the lattice on the image_draw """
        for p in self.polygons:
            p.draw(image_draw)

    def debug_print(self):
        """ Print debug informations about the lattice """
        print("Polygons:")
        print(self.polygons)
        print("\n")
        print("Vertices:")
        print(self.vertices)

    def mutate(self, intensity):
        """ Mutate the vertices that are not on the border of the image """

        # Mutate each vertex that is not in one border or outside the image
        for vertex in self.vertices.values():
            x_coord = vertex.coordinates[0]
            y_coord = vertex.coordinates[1]
            if x_coord != 0 and y_coord != 0 \
                and x_coord < self.image_size[0] and y_coord < self.image_size[1]:
                vertex.random_mutation(intensity)


    def randomise_colors(self):
        """ Randomise the color of each polygon """
        for polygon in self.polygons:
            polygon.set_random_color()

    def gradient_colors(self, color_init, color_final, polygon_sort_key=None):
        """
        Apply a gradient of colors to the polygons, by iterating on
        them after applying a sorting function before (optional)
        """
        polygons_count = len(self.polygons)

        delta_r = (color_final[0] - color_init[0]) / polygons_count
        delta_g = (color_final[1] - color_init[1]) / polygons_count
        delta_b = (color_final[2] - color_init[2]) / polygons_count

        color_current = color_init

        # Optionally sort the polygon list
        if polygon_sort_key:
            polygon_list = sorted(self.polygons, key=polygon_sort_key)
        else:
            polygon_list = self.polygons

        # Iterate over sorted polygon list, color them and update current color
        for polygon in polygon_list:
            color_current_int = (
                int(color_current[0]),
                int(color_current[1]),
                int(color_current[2])
            )

            polygon.color = color_current_int

            color_current = (
                color_current[0] + delta_r,
                color_current[1] + delta_g,
                color_current[2] + delta_b
            )

    def gradient_colors_direction(self, color_init, color_final, angle):
        """ Apply a gradient of color according to a certain angle """
        # Define the sorting function according to the given angle
        def polygon_sort_key(polygon):
            center = polygon.center

            # Order the polygons following the angle
            return cos(angle) * center[0] + sin(angle) * center[1]

        # Pass the sorting function to gradient_colors()
        self.gradient_colors(color_init, color_final, polygon_sort_key)


    def gradient_colors_random_direction(self, color_init, color_final):
        """ Apply a gradient of color according to a random angle """
        # Choose angle at random, from 0 to 2PI radians
        angle = random() * 2 * pi

        self.gradient_colors_direction(color_init, color_final, angle)

    def initialise(self, separate_in_triangles=False):
        """
        Initialise the lattice with simple rectangles, cutting the image
        evenly considering self.polygon_counts. If separate_in_triangles is
        True, cuts those rectangles in half to make triangles
        """

        # Construct the lattice with rectangles
        for i in range(0, self.polygon_counts[0]):
            for j in range(0, self.polygon_counts[1]):
                rect_coordinates = [
                    (i * self.polygon_sizes[0], j * self.polygon_sizes[1]),
                    ((i + 1) * self.polygon_sizes[0], j * self.polygon_sizes[1]),
                    ((i + 1) * self.polygon_sizes[0], (j + 1) * self.polygon_sizes[1]),
                    (i * self.polygon_sizes[0], (j + 1) * self.polygon_sizes[1])
                ]

                rect_vertices = []

                # Transform each (x, y) coordinate in the object Vertex(x, y).
                # Makes sure that two rectangles that use the same vertex use
                # the same instance of the Vertex class, to apply mutations to
                # those vertices later.
                for coordinate in rect_coordinates:
                    if coordinate in self.vertices:
                        rect_vertices.append(self.vertices[coordinate])
                    else:
                        new_vertex = Vertex(coordinate)
                        self.vertices[coordinate] = new_vertex
                        rect_vertices.append(new_vertex)

                if separate_in_triangles:
                    # Separate rectangle into two triangles, alternating on
                    # which diagonal to separate
                    if (i + j) % 2:
                        triangle1 = rect_vertices[0:3]
                        triangle2 = [rect_vertices[0]] + rect_vertices[2:4]
                    else:
                        triangle1 = rect_vertices[0:2] + [rect_vertices[3]]
                        triangle2 = rect_vertices[1:4]

                    # Add both triangles to the polygons
                    self.polygons.append(Polygon(triangle1))
                    self.polygons.append(Polygon(triangle2))

                else:
                    # Add new rectangle to the polygons
                    self.polygons.append(Polygon(rect_vertices))
