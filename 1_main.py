class Figure:
    pass
    # def __init__(self) -> None:
        # print("Figure is parent class")

class Point:
    def __init__(self, position_X, position_Y) -> None:
        self.position_X = position_X
        self.position_Y = position_Y

    def __add__(self, __o):
        return self.position_X + __o.position_X, self.position_Y + __o.position_Y
    def __sub__(self, __o):
        return  self.position_X - __o.position_X, self.position_Y - __o.position_Y


class Rectangle(Figure, Point):
    def __init__(self,__point1, __point2, position_X = 0, position_Y = 0) -> None:
        Figure.__init__(self)
        Point.__init__(self, position_X, position_Y)
        self.__point1 = __point1
        self.__point2 = __point2

    ob1 = None
    def square(self):
        self.ob1 = self.__point1 - self.__point2
        return self.ob1


    def __str__(self) -> str:
        return f"ob1 = {self.square()}"



# class Circle(Figure, Point):
#     pass

# class RightTriangle(Figure, Point):
#     pass

# class Trapezoid(Figure, Point):
#     pass

f1 = Figure()

p1 = Point(5,5)
p2 = Point(2,2)

r1 = Rectangle(p1,p2)
print(r1)

