import time

def miernik_wykonania(f):
    licznik_wywolania = 0

    def monitorowana(n):
        nonlocal licznik_wywolania
        licznik_wywolania += 1

        start = time.time()
        wynik = f(n)
        koniec = time.time()

        czas_wykonania = koniec - start

        print(f"Czas wykonania: {czas_wykonania: .6f} sekund")
        print(f"Liczba wywołań: {licznik_wywolania}")

        return wynik

    return monitorowana


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)
    
monitorowana_silnia = miernik_wykonania(silnia)

print(monitorowana_silnia(5))

print(monitorowana_silnia(6))
