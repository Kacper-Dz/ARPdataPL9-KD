# Napisz funkcje, która zwróci "odwrotny" indeks wybranego indeksu i tekstu
#       Przyjmowane argumenty:
#       - Łańcuch znaków
#       - indeks (z przedziału podane tekstu)
#       Zwraca:
#       - odwrotny indeks

def odwrotny(txt, index):
    if 0 <= index <= (len(text) - 1):
        return index - len(txt)
    else:
        return "Błąd! Zła wartość indeksu."

text = input("Proszę podać dowolny łańcuch znaków: ")
indexx = int(input("Proszę podać dowolny indeks: "))

print("Odwrócony indeks to:", odwrotny(text, indexx))
