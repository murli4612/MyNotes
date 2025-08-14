import math 
class Shape:
    def __init__(self,colour):
        self.colour = colour
    
    def area(self):
        raise NotImplementedError("sub class must implement area method")

class Circle(Shape):
    def __init__(self,colour,radius):
        super().__init__(colour)
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, colour,length,width):
        super().__init__(colour)
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

circle_instance = Circle("Red", 5)
rectangle_instance = Rectangle("Black",8,9)
print(circle_instance.area())
print(rectangle_instance.area())
        