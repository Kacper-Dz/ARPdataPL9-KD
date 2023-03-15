# Napisz funkcję manage_list, która przyjmuje dwa argumenty:
#    - opcja: dodaj, usuń
#    - Wartość
# Jeżeli wybraliśmy dodaj, wykonany jest append
# Jeżeli usuń - wykonujemy pop()
# Funkcja niczego nie zwraca

animals = ["Kot", "Pies", "Słoń", "Zółw", "Chomik", "Papuga"]

# def manage_list(lista, opcja):
#     if opcja == "dodaj":
#         wartosc = input("O jaki element chcesz rozszerzyć listę?: ")
#         lista.append(wartosc)
#     elif opcja == "usuń":
#         lista.pop()
#     else:
#         lista.clear()
#         print("Podano niepoprawną opcję")
#
#
# wybor = input("Proszę wpisać co chcesz zrobic z listą: usuń czy dodaj?: ")
# manage_list(animals, wybor)
# print(animals)


def manage_list(option, value):
    if option == "dodaj":
        animals.append(value)
    elif option == "usun":
        animals.pop()
