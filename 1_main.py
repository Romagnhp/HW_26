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
    def __init__(self,__point1, __point2, position_X, position_Y) -> None:
        Figure.__init__(self)
        Point.__init__(self, position_X, position_Y)



class Circle(Figure, Point):
    pass

class RightTriangle(Figure, Point):
    pass

class Trapezoid(Figure, Point):
    pass



