# # Słownik
# contacts = {
#     "Adam": "670234515",
#     "Ewelina": "123456745",
#     "Piotr": "000235423"
# }
# print(len(contacts))
# # Dostep do kluczy
# print(contacts.keys())
# print(contacts.values())
# print(contacts.items())
#
# if "Iza" in contacts.keys():
#     print("Kontakt istnieje.")
#
# # Dodawanie nowych kluczy
# contacts["Iza"] = "123679043"
# # Ten zapis służy do tworzenia nowych oraz edytowania istniejących pozycji
# print(contacts)
# contacts["Adam"] = "000112233"
# print(contacts)
# # Wyświetlanie wybranej wartości
# print(contacts["Ewelina"])
# print(contacts.get("Bożydar", "Nope!!!"))
# # Usuwanie kluczy ( oraz ich wartości)
# contacts.pop("Adam") # W tym przypadku pop nie może być bez arg. - zwraca usuniętą wartość
# del contacts ["Iza"] # - po prostu usuwa
# # Przepisywanie pod nowy klucz
# contacts["Mateusz"] = contacts.pop("Ewelina")
# print(contacts)
#
# # Krotka (tuple)
# metadata = ("Python w DS", "1.0", "15.03.2023", "15.03.2023")
# print(metadata[0], metadata[3], len(metadata))
# print(metadata.count("15.03.2023"))

# Zbiór
numbers = {1, 2, 3, 4, 5, 6, 7, 1, 4, 6}
# Pusty zbiór: n =set()
print(numbers)
numbers.pop()  # Bez argumentu usuwamy ostatni element
numbers.add(7)  # Dodajemy pojedynczy element
numbers.update([12, 1, 4, 5, 2, 0, 11])  # Dodanie listy elementów
print(numbers)
