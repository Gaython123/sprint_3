class Point:
    def __init__(self, coordinate_1: int, coordinate_2:int):
        self.coordinate_1 = coordinate_1
        self.coordinate_2 = coordinate_2

    def __str__(self):
        return f"{self.coordinate_1};{self.coordinate_2}"


class Triangle:
    def __init__(self, name, point_1: Point, point_2: Point, point_3: Point):
        """
        :param name: name of triangle
        :param point_1: first Point with two coordinates
        :param point_2: second Point with two coordinates
        :param point_3: triple Point with two coordinates
        """
        self.name = name
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def __str__(self):
        return f"{self.name} with coordinates: "\
               f"A({self.point_1}),"\
               f"B({self.point_2}),"\
               f"C({self.point_3}),"

    def display(self):
        """
        :return: prints Triangle with its Coordinates
        """

        print(f"{self.name} with coordinates: "
              f"A({self.point_1}),",
              f"B({self.point_2}),",
              f"C({self.point_3})")



    #def square_of_triangle(self):
    #    """
    #    :return: Square of Triangle
#
    #    Square of Triangle with coordinates:
    #    (x1, y1), (x2, y2), (x3, y3)  can be counted by:
    #    S = (x1y2 + x2y3 + x3y1 – x1y3 – x2y1 – x3y2)/2
#
    #    I use abs because on graph 'S' can be <= 0
    #    """
    #    for
    #        return abs((self.
    #def coordinates_increased(self, increasing_index: int):
    #    """
#
    #    :param increasing_index: - Is the index that represents the number of coordinates increasing
    #    :return: Increased coordinates by 'Increasing_index'
    #    if coordinates increased by 'x', then 'S' - Square increases by '3' * 'x'
    #    """
    #    self.point_a_1 *= increasing_index
    #    self.point_a_2 *= increasing_index
    #    self.point_b_1 *= increasing_index
    #    self.point_b_2 *= increasing_index
    #    self.point_c_1 *= increasing_index
    #    self.point_c_2 *= increasing_index

A = Point(3, 7)
B = Point(-2, 9)
C = Point(-4, 22)
ABC = Triangle("ABC", A, B, C)
ABC.display()


#XYZ.coordinates_increased(3)
#XYZ.display()
#print(XYZ.square_of_triangle())
