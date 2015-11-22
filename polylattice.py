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
        for p in self.polygons:
            p.draw(image_draw)

    def debug_print(self):
        print("Polygons:")
        print(self.polygons)
        print("\nVertices:")
        print(self.vertices)

    def mutate(self, intensity):

        # Mutate each vertex that is not in one border of the image
        for vertex in self.vertices.values():
            if vertex.coordinates[0] != 0 \
                    and vertex.coordinates[0] != self.image_size[0] \
                    and vertex.coordinates[1] != 0 \
                    and vertex.coordinates[1] != self.image_size[1]:

                vertex.random_mutation(intensity)

    def randomise_colors(self):
        for polygon in self.polygons:
            polygon.set_random_color()

    def initialise(self):
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
