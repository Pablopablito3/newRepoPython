class Shape():

    def area(self):

        return f"Undefined area{self}"
    
    def __str__(self, shape):
        self.shape = shape
        return f"{Shape}"
    
    
    

class Colored():
    def __init__(self, color):
        self.color = color

    def __str__(self, colored):
        self.colored = colored
        return f"{Colored}"
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius

    def area(self):
        
        return (3.14 * (self.radius)**2)
    
    def __str__(self, shape):
        super().__str__(shape)
        return f'Circle{shape}'
    
class ColoredCircle(Circle, Colored):

    def __init__(self, radius, color):
        super().__init__(radius, color)
        
    def __str__(self, color):
        super().__str__(color)
        return f'Colored Circle of color {self.color}'
    
    def __add__(self, other):
        if isinstance(other, ColoredCircle):
            new_radius = self.radius + other.radius
            new_color = self.color if self.color == other.color else "mixed"

            return ColoredCircle(new_radius, new_color)
        return NotImplemented

    def __mul__(self, other):
        



    




    

