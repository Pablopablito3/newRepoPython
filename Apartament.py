class Apartament:
    def __init__(self, powierzchnia, cena):
        """Inicjalizacja apartamentu"""
        self.powierzchnia = powierzchnia  
        self.cena = cena  

    def __repr__(self):
        """Reprezentacja apartamentu"""
        return f"Apartament(powierzchnia: {self.powierzchnia} m², cena: {self.cena} zł)"

    
    def __eq__(self, other):
        if isinstance(other, Apartament):
            return self.powierzchnia == other.powierzchnia
        return False

   
    def __ne__(self, other):
        if isinstance(other, Apartament):
            return self.powierzchnia != other.powierzchnia
        return False

  
    def __gt__(self, other):
        if isinstance(other, Apartament):
            return self.cena > other.cena
        return False

 
    def __lt__(self, other):
        if isinstance(other, Apartament):
            return self.cena < other.cena
        return False

 
    def __ge__(self, other):
        if isinstance(other, Apartament):
            return self.cena >= other.cena
        return False

 
    def __le__(self, other):
        if isinstance(other, Apartament):
            return self.cena <= other.cena
        return False





apartament1 = Apartament(50, 300000)  
apartament2 = Apartament(50, 350000)  
apartament3 = Apartament(60, 350000) 


print(apartament1 == apartament2)  
print(apartament1 != apartament3)  


print(apartament1 > apartament2)  
print(apartament2 > apartament1)   
print(apartament2 >= apartament3)  
print(apartament1 <= apartament3)  