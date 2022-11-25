from math import fabs, hypot

# абстрактный класс Figure
class Figure:
    def Square(self):
        print("Figure is parent class\n")

class Point:
    def __init__(self, position_X, position_Y) -> None:
        self.position_X = position_X
        self.position_Y = position_Y

    def getHorizonalLine(self, __o):
        return fabs(self.position_X - __o.position_X)
    
    def getVerticalLine(self, __o):
        return fabs(self.position_Y - __o.position_Y)

    def __str__(self) -> str:
        return f"({self.position_X}, {self.position_Y})"


# опредиление прямоугольника по 2_ум тчк. которые составляют диагональ прямоугольника
# тчк p1 -верхний левый угол; тчк p2 - нижний правый угол
class Rectangle(Figure, Point):
    def __init__(self,__point1, __point2, position_X = 0, position_Y = 0) -> None:
        Figure.__init__(self)
        Point.__init__(self, position_X, position_Y)
        self.LeftTopAngle = __point1
        self.RightDownAngle = __point2

    def __int__(self):
        temp1 = Point.getHorizonalLine(self.LeftTopAngle, self.RightDownAngle)
        temp2 = Point.getVerticalLine(self.LeftTopAngle, self.RightDownAngle)
        return int(temp1*temp2)

    def __str__(self) -> str:
        return f"\nrectanguel square - {self.__int__()}, left top angle point - {self.LeftTopAngle}, bottom right angle point - {self.RightDownAngle}"



# опредиление прямоугольного треугольника по 2_ум тчк которые составляют его гипотенузу
# обязательное условие  - катеты прямоугольного треугольника паралельны осям декартовой системы координат
# тчк p1 -верхний левый угол; тчк p2 - нижний правый угол
class RightTriangle(Figure, Point):
    def __init__(self, __point1, __point2, position_X = 0, position_Y = 0) -> None:
        Figure.__init__(self)
        Point.__init__(self, position_X, position_Y)
        self.LeftTopAngle = __point1
        self.RightDownAngle = __point2

    def __int__(self):
        temp1 = Point.getHorizonalLine(self.LeftTopAngle, self.RightDownAngle)
        temp2 = Point.getVerticalLine(self.LeftTopAngle, self.RightDownAngle)
        return int((temp1*temp2)/2)

    def __str__(self) -> str:
        return f"right triangle square - {self.__int__()}, left top angle point - {self.LeftTopAngle}, bottom right angle point - {self.RightDownAngle}"



# опредиление окружности по 2_ум тчк. Первая тчк. - центр окружности, Вторая тчк. - лежит на окружности
class Circle(Figure, Point):
    def __init__(self, __point1, __point2, position_X = 0, position_Y = 0) -> None:
        Figure.__init__(self)
        Point.__init__(self, position_X, position_Y)
        self.centrPointCircl = __point1
        self.PointOnCircl = __point2

    def funcRadius(self):
        axisProjection_X = Point.getHorizonalLine(self.centrPointCircl, self.PointOnCircl)
        axisProjection_Y = Point.getVerticalLine(self.centrPointCircl, self.PointOnCircl)
        return hypot(axisProjection_X, axisProjection_Y)

    def __int__(self):
        return int(2* 3.14 * self.funcRadius())

    def __str__(self):
        return f"circle square - {self.__int__()}, radius of circle {self.funcRadius():.2f}, center of circle  - {self.centrPointCircl}"

# задание трапеции по 4_ем точкам
class Trapezoid(Figure, Point):
    def __init__(self, __point1, __point2, __point3, __point4, position_X = 0, position_Y =0) -> None:
        Figure.__init__(self)
        Point.__init__(self, position_X, position_Y)
        self.point1 = __point1
        self.point2 = __point2
        self.point3 = __point3
        self.point4 = __point4

        self.topBase = None
        self.lowBase = None
        self.hight = None

    def __int__(self):
        self.topBase = Point.getHorizonalLine(self.point1, self.point3)
        self.lowBase = Point.getHorizonalLine(self.point4, self.point2)
        self.hight = Point.getVerticalLine(self.point1, self.point2)
        return int(((fabs(self.topBase) + fabs(self.lowBase)) /2) * self.hight)

    def __str__(self) -> str:
        return f"trapezoid square - {self.__int__()}, top base - {self.topBase}, low base - {self.lowBase}, hight of trapezoid - {self.hight}" 

# тчк. для формирования гееметрических фигур
p1 = Point(10, 30)
p2 = Point(25, 25)
p3 = Point(20, 30)
p4 = Point(5, 25)

# Прямоугольник 
r1 = Rectangle(p1, p2)
# вызов перегруженного метода int 
int(r1)
# вывод инф. о фигуре через перегруженный метод str
print(r1)
# вызов родительского метода Square()
r1.Square()

# Треугольный прямоугольник
t1 = RightTriangle(p1, p2)
# вызов перегруженного метода int 
int(t1)
# вывод инф. о фигуре через перегруженный метод str
print(t1)
# вызов родительского метода Square()
t1.Square()

# Окружность
c1 = Circle(p1, p2)
# вызов перегруженного метода int 
int(c1)
# вывод инф. о фигуре через перегруженный метод str
print(c1)
# вызов родительского метода Square()
c1.Square()

# Трапеция
tr1 = Trapezoid(p1, p2, p3, p4)
# вызов перегруженного метода int 
int(tr1)
# вывод инф. о фигуре через перегруженный метод str
print(tr1)
# вызов родительского метода Square()
tr1.Square()