class Samolot:
    def __init__(self, typ, max_pasażerowie, pasażerowie=0):
        """Inicjalizacja samolotu"""
        self.typ = typ  
        self.max_pasażerowie = max_pasażerowie  
        self.pasażerowie = pasażerowie  

    def __repr__(self):
        """Reprezentacja samolotu"""
        return f"Samolot({self.typ}, max pasażerowie: {self.max_pasażerowie}, pasażerowie: {self.pasażerowie})"

    
    def __eq__(self, other):
        if isinstance(other, Samolot):
            return self.typ == other.typ
        return False

    
    def __add__(self, number):
        if isinstance(number, int):
            new_pasażerowie = self.pasażerowie + number
            if new_pasażerowie <= self.max_pasażerowie:
                return Samolot(self.typ, self.max_pasażerowie, new_pasażerowie)
            else:
                print("Przekroczono maksymalną liczbę pasażerów!")
                return self  
        return NotImplemented

    
    def __sub__(self, number):
        if isinstance(number, int):
            new_pasażerowie = self.pasażerowie - number
            if new_pasażerowie >= 0:
                return Samolot(self.typ, self.max_pasażerowie, new_pasażerowie)
            else:
                print("Liczba pasażerów nie może być ujemna!")
                return self  
        return NotImplemented

    
    def __iadd__(self, number):
        if isinstance(number, int):
            new_pasażerowie = self.pasażerowie + number
            if new_pasażerowie <= self.max_pasażerowie:
                self.pasażerowie = new_pasażerowie
            else:
                print("Przekroczono maksymalną liczbę pasażerów!")
        return self

    
    def __isub__(self, number):
        if isinstance(number, int):
            new_pasażerowie = self.pasażerowie - number
            if new_pasażerowie >= 0:
                self.pasażerowie = new_pasażerowie
            else:
                print("Liczba pasażerów nie może być ujemna!")
        return self

    
    def __gt__(self, other):
        if isinstance(other, Samolot):
            return self.max_pasażerowie > other.max_pasażerowie
        return NotImplemented

    
    def __lt__(self, other):
        if isinstance(other, Samolot):
            return self.max_pasażerowie < other.max_pasażerowie
        return NotImplemented

    
    def __ge__(self, other):
        if isinstance(other, Samolot):
            return self.max_pasażerowie >= other.max_pasażerowie
        return NotImplemented

    
    def __le__(self, other):
        if isinstance(other, Samolot):
            return self.max_pasażerowie <= other.max_pasażerowie
        return NotImplemented

# Przykład użycia:
samolot1 = Samolot("Boeing 747", 600, 100)  
samolot2 = Samolot("Airbus A380", 800, 200)  

print(samolot1)
print(samolot2)


print(samolot1 == samolot2)  


samolot1 += 50
print(samolot1)  


samolot2 -= 100
print(samolot2)


print(samolot1 > samolot2)  


samolot1 += 500  
print(samolot1)  


print(samolot1 < samolot2)  