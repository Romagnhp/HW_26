import pickle

class Point:
    def __init__(self, pointX, pointY) -> None:
        self.pointX = pointX
        self.pointY = pointY

    def __add__(self, __objPoint):
        return Point(self.pointX + __objPoint.pointX, self.pointY + __objPoint.pointY)

    def __str__(self) -> str:
        return f'({self.pointX}, {self.pointY})'

class Shape(Point):
    def __init__(self,__objPoint, width, height, pointX = 0, pointY = 0,) -> None:
        super().__init__(pointX, pointY)
        self.__leftTopAngle = __objPoint
        self.dimensionHeight = height
        self.dimensionWidth = width

    # метод для доступв к левой верхней тчк в дочерних классах
    def getleftTopAngle(self):
        return self.__leftTopAngle
        
    # сохранение фигуры в файл
    def Save(self):
        with open('shape.dll', mode='wb') as file:
            pickle.dump(self.__leftTopAngle, file)
            pickle.dump(self.dimensionWidth, file)
            pickle.dump(self.dimensionHeight, file)

    # считывание фигуры из файла
    def Load(self):
        with open ('shape.dll', mode='rb') as file:
            temp1 = pickle.load(file)
            temp2 = pickle.load(file)
            temp3 = pickle.load(file)
        return f'Верхняя левая точка фигуры - {temp1},\nгабаритный размер вдоль оси Х - {temp2},\nгабаритный размер вдоль оси Y - {temp3}'

    # вывод на экран информации о фигуре
    def Show(self):
        temp = self.Load()
        print(temp)

class Rectangle(Shape):
        def __init__(self, __objPoint, width, height, pointX=0, pointY=0) -> None:
            super().__init__(__objPoint, width, height, pointX, pointY)
            print("\nфигура  - прямоугольник")

class Square(Shape):
    def __init__(self, __objPoint, width, height, pointX=0, pointY=0) -> None:
        super().__init__(__objPoint, width, height, pointX, pointY)        
        print("\nфигура квадрат")

class Circle(Shape):
    def __init__(self, __objPoint, width, height, pointX=0, pointY=0) -> None:
        super().__init__(__objPoint, width, height, pointX, pointY)
        print('\nфигура окружность')

    def defindPointCenter(self):
        # создание абстрактой тчк.
        # width == height 

        somePoint = Point(self.dimensionWidth/2, self.dimensionHeight/2)
        
        # доступ к верхней левой тчк. через метод дочернего класса Shape
        LeftTopAngle = super().getleftTopAngle()

        # использование перегруженного оператора '+' класса Point
        centerCircl = LeftTopAngle + somePoint
        return centerCircl

    def __str__(self) -> str:
        return f'координаты центра окружности - {self.defindPointCenter()}, радиус - {self.dimensionHeight/2}'

class Ellips(Shape):
    def __init__(self, __objPoint, width, height, pointX=0, pointY=0) -> None:
        super().__init__(__objPoint, width, height, pointX, pointY)
        print('\nфигура эллипс')


# ПРОВЕРКА

point_1 = Point(4,5)
shape_1 = Shape(point_1, 0, 0)

shape_1.Save()
shape_1.Load()
shape_1.Show()

point_2 = Point(6,8)
rectangle_1 = Rectangle(point_2, 10, 50)
rectangle_1.Save()
rectangle_1.Load()
rectangle_1.Show()

point_3 = Point(10, 12)
circle_1 = Circle(point_2, 60, 60)
circle_1.Save()
circle_1.Load()
circle_1.Show()
print(circle_1)