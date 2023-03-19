# Do zadania nr 4 z pracy domowej dopisz zabezpieczenie, jezeli użytkownik podał informację
# której nie można konwertować na int.

try:
    liczba = int(input("Podaj pierwszą liczbę do zsumowania: "))
    suma = 0
    while liczba >= 0:
        liczba = int(input("Podaj kolejną liczbę do zsumowania: "))
        print(f"Nie podano liczby!")
        suma += liczba
    else:
        print("Podana liczba jest ujemna! Suma podanych wcześniej liczb wynosi: ", suma - liczba)

except (TypeError, ValueError):
    print(f"Nie podano liczby!")

# Rozwiń funkcjonalnosć z (opcja, *args) o nową opcję "iloraz".
# Zabezpiecz program, że w przypadku dzielenia przez zero kontunuuj działanie.
# iloraz (dzielenia kolejnych wartości), pomijając błędny (umieść continue w except)


def calculator(action: str, *args):
    if len(args) >= 2:
        result = args[0]
        if action == "add":
            for i in range(1, len(args)):
                result += args[i]
        if action == "multiply":
            for i in range(1, len(args)):
                result *= args[i]
        if action == "substract":
            for i in range(1, len(args)):
                result -= args[i]
        if action == "divide":
            for i in range(1, len(args)):
                try:
                    result /= args[i]
                except ZeroDivisionError:
                    continue
        return result
    else:
        print(f"Podano za mało liczb")
        return args[0]


print(calculator("add", 1, 2, 3))
print(calculator("multiply", 1, 2, 3))
print(calculator("substract", 1, 2, 3))
print(calculator("substract", 1, 2, 3, 0, 4))
