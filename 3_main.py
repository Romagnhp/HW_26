import pickle

class Point:
    def __init__(self, pointX, pointY) -> None:
        self.pointX = pointX
        self.pointY = pointY

class Shape(Point):
    
    def __init__(self, pointX, pointY,) -> None:
        super().__init__(pointX, pointY)
        
    # сохранение фигуры в файл
    def Save(self):

        with open('shape.dll', mode='wb') as file:
            pickle.dump(self.pointX, file)
            pickle.dump(self.pointY, file)
        pass

    # считывание фигуры из файла
    def Load(self):

        with open ('shape.dll', mode='rb') as file:
            X = pickle.load(file)
            Y = pickle.load(file)
        return X, Y

    # вывод на экран информации о фигуре
    def Show(self):
        temp = self.Load()
        print(temp)
    


class Rectangle(Shape):

    def __init__(self, __objPoint, width, higth, pointX = 0, pointY = 0) -> None:
        super().__init__(pointX, pointY)
    
        self.__leftTopAngle = __objPoint
        self.__width = width
        self.__higth = higth

class Square(Rectangle):

    def __init__(self, __objPoint, width, higth, pointX = 0, pointY = 0) -> None:
        super().__init__(__objPoint, width, higth, pointX, pointY)

      
class Circle(Rectangle):

    def __init__(self, __objPoint, width, higth, pointX=0, pointY=0) -> None:
        super().__init__(__objPoint, width, higth, pointX, pointY)


class Ellips(Rectangle):

    def __init__(self, __objPoint, width, higth, pointX=0, pointY=0) -> None:
        super().__init__(__objPoint, width, higth, pointX, pointY)
    pass

point_1 = Point(4,5)
shape_1 = Shape(2,3)

shape_1.Save()
shape_1.Load()
shape_1.Show()

rectangle_1 = Rectangle(point_1, 10, 50)
rectangle_1.Save()
rectangle_1.Load()
rectangle_1.Show()