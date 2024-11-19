class Complex:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real  # część rzeczywista
        self.imag = imag  # część urojona

    def __repr__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"

    # Operator dodawania (a + bi + c + di)
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    # Operator odejmowania (a + bi - c - di)
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        return NotImplemented

    # Operator mnożenia (a + bi) * (c + di)
    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        return NotImplemented

    # Operator dzielenia (a + bi) / (c + di)
    def __truediv__(self, other):
        if isinstance(other, Complex):
            denom = other.real**2 + other.imag**2
            if denom == 0:
                raise ZeroDivisionError("Cannot divide by zero complex number")
            real_part = (self.real * other.real + self.imag * other.imag) / denom
            imag_part = (self.imag * other.real - self.real * other.imag) / denom
            return Complex(real_part, imag_part)
        return NotImplemented

    # Operator równości (a + bi == c + di)
    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.real == other.real and self.imag == other.imag
        return False

    # Metoda zwracająca moduł liczby zespolonej (sqrt(a^2 + b^2))
    def modulus(self):
        return (self.real**2 + self.imag**2)**0.5

    # Metoda zwracająca argument liczby zespolonej (kąt w układzie biegunowym)
    def argument(self):
        import math
        return math.atan2(self.imag, self.real)

# Przykład użycia:
z1 = Complex(3, 4)  # liczba zespolona 3 + 4i
z2 = Complex(1, -2) # liczba zespolona 1 - 2i

print(f"z1 = {z1}")
print(f"z2 = {z2}")

# Dodawanie
z3 = z1 + z2
print(f"z1 + z2 = {z3}")

# Odejmowanie
z4 = z1 - z2
print(f"z1 - z2 = {z4}")

# Mnożenie
z5 = z1 * z2
print(f"z1 * z2 = {z5}")

# Dzielenie
z6 = z1 / z2
print(f"z1 / z2 = {z6}")

# Moduł liczby zespolonej
print(f"Moduł z1 = {z1.modulus()}")

# Argument liczby zespolonej (kąt w układzie biegunowym)
print(f"Argument z1 = {z1.argument()}")