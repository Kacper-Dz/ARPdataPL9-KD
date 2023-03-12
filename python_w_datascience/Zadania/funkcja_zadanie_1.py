# Napisz funkcje is_even która przyjmuje jeden argument, która zwraca True - jeżeli liczba jest parzysta
# a wprzeciwnym razie False
# Wykorzystaj funkcje od poprzedniego zadania

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


liczba = int(input("Podaj proszę liczbę: "))
if is_even(liczba) is True:
    print("Liczba jest parzysta!")
elif is_even(liczba) is False:
    print("Liczba jest nieparzysta!")

# # Rozwiazanie od Trenera:
# def is_even(a):
#         return a % 2 == 0
#
#
# liczba = int(input("Podaj proszę liczbę: "))
# if is_even(liczba):
#     print("Liczba jest parzysta!")
# else:
#     print("Liczba jest nieparzysta!")
