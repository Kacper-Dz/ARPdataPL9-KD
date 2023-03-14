# Lista
animals = ["Kot", "Pies", "Słoń", "Zółw", "Chomik", "Papuga"]
values = [3, 4.67, "LoL", True, 11, "xD"]            # Tak nie robimy, lepiej nieszać typów danych w ramach jednej listy
# Pusta lista: empty = [] lub empty=list()
# Metody - funkcje listy
print(len(animals))
print(animals[0], animals[-1], animals[2:4])
# Funkcje agregujące
numbers = [2, 5, 10, 3]
print(sum(numbers), max(numbers), min(numbers))
# Dodawanie
animals.append("Szynszyla")
print(animals)
animals.extend(["Mysz", "Kanarek"])
print(animals)
animals.insert(1, "Krokodyl")
print(animals)
# Usuwanie
animals.remove("Szynszyla")
print(animals)
deleted_args = []

deleted_args.append(animals.pop())  # Jeżeli nie podamy idx, usuwamy ostatni element
print(animals)
animals.pop(2)
print(animals)
deleted_value = animals.pop(0)  # Dzięki temu możemy zrobić listę usuniętych danych
deleted_args.append(deleted_value)
print(animals, deleted_args)
# Modyfikacje
animals[0] = "Mrówka"  # Nadpisanie listy
print(animals)
