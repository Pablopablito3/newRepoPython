import math

class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def circumference(self): 
        return 2 * math.pi * self.radius


    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False


    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() > other.circumference()
        return False

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() < other.circumference()
        return False


    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.circumference() >= other.circumference()
        return False


    def __le__(self, other):
        if isinstance(other, Circle):
            return self.circumference() <= other.circumference()
        return False


    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        return NotImplemented


    def __sub__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius - value)
        return NotImplemented


    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            return self
        return NotImplemented


    def __isub__(self, value):
        if isinstance(value, (int, float)):
            self.radius -= value
            return self
        return NotImplemented

    def __repr__(self):
        return f"Circle(radius={self.radius})"



circle1 = Circle(5)
circle2 = Circle(3)
circle3 = Circle(5)


print(circle1 == circle3)  
print(circle1 == circle2)  


print(circle1 > circle2)   
print(circle1 < circle2)   
print(circle1 >= circle3)  
print(circle1 <= circle2)  


circle1 += 2
print(circle1)  

circle1 -= 1
print(circle1)  

circle4 = circle1 + 3
print(circle4)  

circle5 = circle1 - 2
print(circle5)  