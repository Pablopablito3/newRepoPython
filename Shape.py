import math

# Klasa bazowa
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        
        raise NotImplementedError("Metoda 'area' musi być zaimplementowana w klasie pochodnej.")
    


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height



class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2



class RightTriangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height



class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        super().__init__()
        self.base1 = base1
        self.base2 = base2
        self.height = height
    
    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height



rectangle = Rectangle(5, 10)
circle = Circle(7)
triangle = RightTriangle(6, 8)
trapezoid = Trapezoid(4, 6, 5)


print(f"Pole prostokąta: {rectangle.area()}")  
print(f"Pole okręgu: {circle.area():.2f}")  
print(f"Pole trójkąta prostokątnego: {triangle.area()}")  
print(f"Pole trapezu: {trapezoid.area()}")  
