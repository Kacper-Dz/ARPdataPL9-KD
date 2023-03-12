# Napisze funkcje my-pow, która pozowli na zwrócenie potęgi wybranej liczby do wybranej potęgi.
# Liczbe oraz potege podajemy jako argumenty do tej funkcji

def my_pow(x, y):
    return x ** y


a = int(input("Podaj liczbe, która zostanie podniesiona do potęgi: "))
b = int(input("Podaj liczbę, która będzie potęgą: "))
print("Wynik potęgowania to:", my_pow(a, b))
