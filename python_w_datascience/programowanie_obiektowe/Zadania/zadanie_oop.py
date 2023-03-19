# Zadanie 1
# Napisz klasę student, która posiada poozycje argumenty:
#       - imię (str)
#       - nazwisko (str)
#       - lista ocen (list)
#       - średnia ocena (float)

# Powyższe zmienne są zdefiniowane za pomocą __init__. dla każdego nowego obiektu klasy student lista ocen jest pusta,
# a średnia równa się 0.0

# Dodatkowo dopisz funkcję add_grade, która pozwala dodawac do listy ocenę ze zbioru:
# (2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)
# oraz automatycznie przelicza średnią.

# Zadanie 2
# dodać magic functions:
#       - dla str, aby wyświetlić studenta w formacie: "Imie nazwisko - średnia"
#       - dla int - suma ocen
#       - dla float - srednia ocen

class Student:
    def __init__(self, imie, nazwisko):
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.listocen: list = []
        self.sredniaocena: float = 0.0

    def dopisz(self, wybor):
        zbior = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
        if wybor in zbior:
            self.listocen.append(wybor)
            self.sredniaocena = sum(self.listocen) / len(self.listocen)
            print(f"Ocena {wybor} została dodana.")
        else:
            print(f"Ocena {wybor} nie może być wprowadzona.")

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.sredniaocena}"

    def __int__(self):
        return int(sum(self.listocen))

    def __float__(self):
        return self.sredniaocena


s139605 = Student("XXXXX", "YYYYYY")
s139605.dopisz(5.0)
s139605.dopisz(4.0)
s139605.dopisz(2.0)
s139605.dopisz(1.0)
print(str(s139605))
print(int(s139605))
print(float(s139605))
# print(f"Aktualne oceny studenta {s139605.imie} {s139605.nazwisko}: {s139605.listocen}")
# print(f"Ich średnia wynosi: {s139605.sredniaocena}")

