# Przykład na to, że samo użycie nazwy funkcji wystarczy do jej uruchomienia, nie trzeba jej wywoływać
# Ten skrypt działa trochę jak dekorator
# Użycie aliasu ra automatycznie wywołuje funkcje

from figures.flat import *

aliases = {
    "ra": rectangle_area,
    "rc": rectangle_circuit
}

# rectangle area(10, 10)
print(aliases.get("xx", print)(10, 10))
