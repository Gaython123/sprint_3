class Triangle:
    def __init__(self, name,
                 point_a_1: int, point_a_2: int,
                 point_b_1: int, point_b_2: int,
                 point_c_1: int, point_c_2: int):
        self.name = name
        self.point_a_1 = point_a_1
        self.point_a_2 = point_a_2
        self.point_b_1 = point_b_1
        self.point_b_2 = point_b_2
        self.point_c_1 = point_c_1
        self.point_c_2 = point_c_2

    def display(self):
        print(f"{self.name} with coordinates: "
              f"A({self.point_a_1};{self.point_a_2}),",
              f"B({self.point_b_1};{self.point_b_2}),",
              f"C({self.point_c_1};{self.point_c_2}),")

    def __str__(self):
        return f"{self.name} with coordinates: "f"A({self.point_a_1};{self.point_a_2}),"\
               f"B({self.point_b_1};{self.point_b_2}),"\
               f"C({self.point_c_1};{self.point_c_2}),"

#(x1, y1), (x2, y2), (x3, y3)  A = (x1y2 + x2y3 + x3y1 – x1y3 – x2y1 – x3y2)/2.
    def square_of_triangle(self):
        #abs bo if S < 0
        return abs((self.point_a_1*self.point_b_2 + self.point_b_1*self.point_c_2 + self.point_c_1 *self.point_a_2
                - self.point_a_1*self.point_c_2 - self.point_b_1*self.point_a_2 - self.point_c_1*self.point_b_2)/2)


ABC = Triangle("ABC", 1, 2, 3, 4, 5, 6)
XYZ = Triangle("xuz", 3, -1, 4, 8, 11, -7)
ABC.display()
ABC.square_of_triangle()
XYZ.display()
XYZ.square_of_triangle()
print(ABC.square_of_triangle())
print(XYZ.square_of_triangle())