# Napisz klase Animal, która zawiera pola:
#       - legs_count (float)
#       - eyes_count (float)
#       - name (str)
#       - is_alive (Zawsze domylsne True - dla każdego boiektu)

# Dopisz do niej funkcje:
#   __str__ - zwraca nazwę zwierzaka

class Animal:
    def __init__(self, legs_count, eyes_count, name, weight):
        self.legs_count: float = legs_count
        self.eyes_count: float = eyes_count
        self.name: str = name
        self.is_alive = True
        self.weight: float = weight

    def __str__(self):
        return self.name
    def runnning(self):
        return f"{self.name} - tup tup tup tup tup"

class Dog(Animal):
    def __init__(self, legs_count, eyes_count, name, race, weight):
        super().__init__(legs_count, eyes_count, name, weight)
        self.race: str = race

    def __str__(self):
        return f"{super().__str__()} - {self.name} - {self.race}"

d1 = Dog(4, 2, "Azor", "Husky", 56.7)
print(d1.is_alive, d1.race)
print(d1)
print(d1.runnning())