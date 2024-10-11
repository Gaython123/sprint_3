class Point:
    def __init__(self, coordinate_1: int, coordinate_2:int):
        """
        :param coordinate_1: first coordinate of certain point
        :param coordinate_2: second coordinate of certain point
        """
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
               f"C({self.point_3})"

    def display(self):
        """
        :return: prints Triangle with its Coordinates
        """

        print(f"{self.name} with coordinates: "
              f"A({self.point_1}),",
              f"B({self.point_2}),",
              f"C({self.point_3})")


    def square_of_triangle(self):
        """
        :return: Square of triangle by its coordinates

        I use abs because on graph 'S' can be <= 0

        Square of Triangle with coordinates:
        (x1, y1), (x2, y2), (x3, y3)  can be counted by:
        S = (x1y2 + x2y3 + x3y1 – x1y3 – x2y1 – x3y2)/2
        """
        for self.coordinates in self.name:                                                                                                                      #(x1y2 + x2y3 + x3y1 – x1y3 – x2y1 – x3y2)/2
            return abs((self.point_1.coordinate_1 * self.point_2.coordinate_2
                    + self.point_2.coordinate_1 * self.point_3.coordinate_2
                    + self.point_3.coordinate_1 * self.point_1.coordinate_2
                    - self.point_1.coordinate_1 * self.point_3.coordinate_2
                    - self.point_2.coordinate_1 * self.point_1.coordinate_2
                    - self.point_3.coordinate_1 * self.point_2.coordinate_2)/2)

    def coordinates_increased(self, increasing_index: int):
        """
        :param increasing_index: number of increasing every coordinate
        :return: Triangle with the same name but with changed coordinates, increased or decreased by 'increasing_index'
        if coordinates increased by 'x', then 'S' - Square increases by '3' * 'x'
        """
        self.point_1.coordinate_1 *= increasing_index
        self.point_1.coordinate_2 *= increasing_index
        self.point_2.coordinate_1 *= increasing_index
        self.point_2.coordinate_2 *= increasing_index
        self.point_3.coordinate_1 *= increasing_index
        self.point_3.coordinate_2 *= increasing_index
        return Triangle

class Triangle_(Triangle):
    def __init__(self, name, point_1: Point, point_2: Point, point_3: Point, type_of_triangle: str):
        super().__init__(name, point_1, point_2, point_3)
        self.type_of_triangle = type_of_triangle

    def __str__(self):
        return f"{self.name} with coordinates: "\
               f"A({self.point_1}),"\
               f"B({self.point_2}),"\
               f"C({self.point_3}) is {self.type_of_triangle}"

    def display(self):
        print(f"'{self.name}' is '{self.type_of_triangle}' triangle")

    #def triangle_type(self):


A = Point(3, 7)
B = Point(-2, 9)
C = Point(-4, 22)
ABC = Triangle("ABC", A, B, C)
ABC.square_of_triangle()
print(ABC.square_of_triangle())
ABC.display()
ABC.coordinates_increased(2)
ABC.display()
print(ABC.square_of_triangle())


