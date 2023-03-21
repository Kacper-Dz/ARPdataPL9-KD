# Zadanie 1
# Napisz funkcję, która jak argument listę liczby całkowitych, a zwraca wartość int jako
# największa liczba z listy (nie wolno używać max)
# Dodatkowo zabezpiecz program przed blednymi danymi

def maximum(*args) -> int:
    maxi = args[0]
    for i in range(1, len(args)):
        try:
            if args[i] > maxi:
                maxi = args[i]
        except TypeError:
            continue
    return int(maxi)

# Zadanie 2
# Napisz moduł, który będzie posiadał funkcje obliczające:
#       - Funkcję kwadratową (zwraca listę rozwiązań)
#       - Pierwiastek drugiego stopnia z podanej liczby
#       - N element ciągu harmonicznego (prośba o weryfikację czym jest ciąg z netem)

# Wzór y= a*x^2 + b^x +c


def quadratic_func(a: float, b: float, c: float):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b - (delta ** 0.5)) / 2
        x2 = (-b + (delta ** 0.5)) / 2
        return x1, x2
    if delta == 0:
        x1 = -b / (2 * a)
        return x1
    if delta < 0:
        return None


def second_element(number: float) -> float:
    return number ** 0.5


def harmonic_func(element: int) -> float:
    if type(element) == int and element > 0:
        return 1 / element


# Zadanie 3
# Napisz program, który narysuje trójkąt od zależnie podanego n
# Np dla n = 3
# *
# **
# ***
# Dodaj dekorator, który dodatkowo dopisze "-------------" na dole trójkąta oraz policzy liczbę *


def line_decorator(func):
    def wrapper(*args):
        func(*args)
        print("-------------")
        print(f"Number of stars: {int((int(*args) * (int(*args) + 1)) / 2)}")
    return wrapper


@line_decorator
def triangle_print(n: int):
    for i in range(1, n + 1):
        print(i * "*")
    return n


triangle_print(3)
