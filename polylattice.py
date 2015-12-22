from polygon import Vertex, Polygon

class PolyLattice:
    """
    A lattice of polygons, with polygon_counts describing the number of polygons
    on each axis.
    """

    def __init__(self, image_size, polygon_counts):
        self.image_size = image_size
        self.polygon_counts = polygon_counts

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

        # Find border coordinates
        # It is not simply image_size[0] and [1] because the image is not always
        # perfectly divided by the polygons

        # TODO do it

        # Mutate each vertex that is not in one border of the image
        for vertex in self.vertices.values():
            if vertex.coordinates[0] != 0 and \
               vertex.coordinates[0] != self.image_size[0] and \
               vertex.coordinates[1] != 0 and \
               vertex.coordinates[1] != self.image_size[1]:

                vertex.random_mutation(intensity)

    def randomise_colors(self):
        """ Randomise the color of each polygon """
        for polygon in self.polygons:
            polygon.set_random_color()

    def gradient_colors(self, color_init, color_final):
        """
        Apply a gradient of colors to the polygons, by simply iterating on
        them
        """
        n_polygons = len(self.polygons)

        delta_r = int((color_final[0] - color_init[0]) / n_polygons)
        delta_g = int((color_final[1] - color_init[1]) / n_polygons)
        delta_b = int((color_final[2] - color_init[2]) / n_polygons)

        color_current = color_init

        for polygon in self.polygons:
            polygon.set_color(color_current)

            color_current = (
                color_current[0] + delta_r,
                color_current[1] + delta_g,
                color_current[2] + delta_b
            )



    def initialise(self):
        """
        Initialise the lattice with simple rectangles, cutting the image
        evenly considering self.polygon_counts.
        """
        # X and Y size of rectangles
        rect_size = \
        (
            int(self.image_size[0] / self.polygon_counts[0]),
            int(self.image_size[1] / self.polygon_counts[1])
        )

        # Construct the lattice with rectangles
        for i in range(0, self.polygon_counts[0]):
            for j in range(0, self.polygon_counts[1]):
                rect_coordinates = [
                    (i * rect_size[0], j * rect_size[1]),
                    ((i + 1) * rect_size[0], j * rect_size[1]),
                    ((i + 1) * rect_size[0], (j + 1) * rect_size[1]),
                    (i * rect_size[0], (j + 1) * rect_size[1])
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

                # Add new rectangle to the polygons
                self.polygons.append(Polygon(rect_vertices))
