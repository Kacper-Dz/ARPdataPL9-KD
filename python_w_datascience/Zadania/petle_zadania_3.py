# Napisz program, gdzie użytkownik podaje liczbę n (int)
# Następnie program wyświetla wszystkie liczby parzyste od 0 do n (włącznie)

liczba = int(input("Podaj liczbę: "))
for c in range (liczba):
    if c % 2 == 0:
        print("liczba: ", c)

# Wykorzystując pętle while program wyświetli wszytskie pierwiastki liczb od 10 do 2 (włącznie) (n ** 0.5)

n = 10
while n >= 2:
    print("Pierwiastek liczby", n, "to:", n ** 0.5)
    n -= 1

# Napisz program, który sumuje wszytskie liczby całkowite z danego przedziału.
# Początek i koniec podaje użytkownik
# Np. start = 10, end = 12, wynik = 33

lower = int(input("Podaj liczbę początkową: "))
upper = int(input("Podaj liczbę końcową: "))
suma = lower
for c in range(upper - lower):  # alternatywa -> range (lower, upper + 1)
    suma += lower + c + 1       # suma += lower + c
print(suma)

# Rozwiazanie alternatywne, najlepsze
for i in range(lower, upper + 1):
    result += i
print("Wynik", result)

