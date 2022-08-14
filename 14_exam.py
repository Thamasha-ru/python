class Polygon:
    
    def __init__(self):
        self.__width = None
        self.__height = None

    def setwidth(self, width):
        self.__width = width

    def setheight(self, height):
        self.__height = height

    def getwidth(self):
        return self.__width

    def getheight(self):
        return self.__height

class Rectangle(Polygon):
    def area(self):
        return self.getheight() * self.getwidth() 

class Square(Polygon):
    def area(self):
        return self.getheight() ** 2

class Triangle(Polygon):
    def area(self):
        return self.getheight()*self.getwidth() *0.5

rec = Rectangle()
rec.setheight(5)
rec.setwidth(10)

squa = Square()
squa.setheight(7)
squa.setwidth(7)

tria = Triangle()
tria.setheight(8)
tria.setwidth(8)

print("Rectangle area : ", rec.area())
print("Square area : ", squa.area())
print("Triangle area : ", tria.area())

