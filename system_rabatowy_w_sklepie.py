def stworz_rabat(procent_rabatu):
    def cena_po_obnizce(kwota):
        return kwota - (procent_rabatu * 0.01 * kwota)  
    
    return cena_po_obnizce

black_friday_rabat = stworz_rabat(10)

print(black_friday_rabat(180))
print(black_friday_rabat(1270))
print(black_friday_rabat(123))
print(black_friday_rabat(163))
print(black_friday_rabat(246))