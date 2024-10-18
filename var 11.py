import math
class Point:
    def __init__(self, coordinate_1: int, coordinate_2:int):
        self.coordinate_1 = coordinate_1
        self.coordinate_2 = coordinate_2

    def __str__(self):
        return f"{self.coordinate_1};{self.coordinate_2}"

class Triangle:
    def __init__(self, name, point_1: Point, point_2: Point, point_3: Point):
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
        """
        :return: displays triangle's name and type
        """
        print(f"'{self.name}' is '{self.type_of_triangle}' triangle")

    def triangle_type(self):
        """
        :return: returns the lengths of sides (based on it
        we can define what type  of triangle is it
        """
        side_12 = math.sqrt((self.point_2.coordinate_1 - self.point_1.coordinate_1) ** 2 + (self.point_2.coordinate_2 - self.point_1.coordinate_2) ** 2)
        side_13 = math.sqrt((self.point_3.coordinate_1 - self.point_1.coordinate_1) ** 2 + (self.point_3.coordinate_2 - self.point_1.coordinate_2) ** 2)
        side_23 = math.sqrt((self.point_3.coordinate_1 - self.point_2.coordinate_1) ** 2 + (self.point_3.coordinate_2 - self.point_2.coordinate_2) ** 2)

        if side_12 == side_13 == side_23:
            return "Рівносторонній"

        elif (side_12 == side_13 and side_12 != side_23
           or side_12 == side_23 and side_12 != side_13
           or side_13 == side_23 and side_13 != side_12):
             return "Рівнобедренний"

        elif (side_12 ** 2 + side_13 ** 2 == side_23 ** 2
           or side_12 ** 2 + side_23 ** 2 == side_13 ** 2
           or side_13 ** 2 + side_23 ** 2 == side_12 ** 2):
            return "Прямокутний"

        else:
            return "Довільний"

class Triangles:
    def __init__(self):
        self.triangles = []

    def __str__(self):
        return f"{self.triangles}"

    def add_triangle(self, triangle:Triangle_):
        if triangle in self.triangles:
            return

        self.triangles.append(triangle)

    def show_triangle_square_and_type(self, type_of_triangle:str ):
        triangles_type_list = []
        for triangle in self.triangles:
            if type_of_triangle == triangle.triangle_type():
                triangles_type_list.append(f"{triangle.name}: {triangle.square_of_triangle()} cm^2, type is {triangle.triangle_type()}")

        return triangles_type_list

A = Point(3, 7)
B = Point(-2, 9)
C = Point(-4, 22)
D = Point(-9, -10)
ABC = Triangle_("ABC", A, B, C, 0)
XYZ = Triangle_("popa", A, B, D,0)

new_list = Triangles()
new_list.add_triangle(ABC)
new_list.add_triangle(XYZ)

print(new_list.show_triangle_square_and_type("Довільний"))
print(new_list.show_triangle_square_and_type("Рівнобедренний"))