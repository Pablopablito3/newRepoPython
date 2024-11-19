import math


class Shape:
    def __init__(self):
        pass
    
    def area(self):
        """Metoda bazowa do obliczania pola. Będzie nadpisywana przez klasy pochodne."""
        raise NotImplementedError("Metoda 'area' musi być zaimplementowana w klasie pochodnej.")
    
    def __int__(self):
        """Metoda zwracająca pole powierzchni jako liczbę całkowitą."""
        return int(self.area())
    
    def __str__(self):
        """Metoda zwracająca tekstową reprezentację kształtu."""
        return f"Shape (niezdefiniowany kształt)"



class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"Prostokąt (szerokość: {self.width}, wysokość: {self.height})"



class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Okrąg (promień: {self.radius})"



class RightTriangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def __str__(self):
        return f"Trójkąt prostokątny (podstawa: {self.base}, wysokość: {self.height})"


# Klasa Trapez
class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        super().__init__()
        self.base1 = base1
        self.base2 = base2
        self.height = height
    
    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height
    
    def __str__(self):
        return f"Trapez (podstawa 1: {self.base1}, podstawa 2: {self.base2}, wysokość: {self.height})"





rectangle = Rectangle(5, 10)
circle = Circle(7)
triangle = RightTriangle(6, 8)
trapezoid = Trapezoid(4, 6, 5)


print(f"Pole prostokąta: {rectangle.area()}")  
print(f"Pole okręgu: {circle.area():.2f}")  
print(f"Pole trójkąta prostokątnego: {triangle.area()}")  
print(f"Pole trapezu: {trapezoid.area()}") 


print(f"Pole prostokąta (jako int): {int(rectangle)}") 
print(f"Pole okręgu (jako int): {int(circle)}")  


print(f"Reprezentacja prostokąta: {str(rectangle)}")
print(f"Reprezentacja okręgu: {str(circle)}")
print(f"Reprezentacja trójkąta prostokątnego: {str(triangle)}")
print(f"Reprezentacja trapezu: {str(trapezoid)}")