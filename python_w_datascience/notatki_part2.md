# Python w Data Science - part 2
## Pętla while

W ramach pętli while musimy pamiętać o zmianie wartości elementu sterującego pętlą. Pętla będzie działać 
w nieskończoność.
```
n = 0
while n < 10:
    print(n ** 2)
    n += 1
```
## Funkcjonalności w pętlach

Instrukcje działają dla while oraz for:
1. break - kończy pracę całej pętli, np.
```
n = 10
while n > 0:
    if n == 4:
        break
    print("n=", n)
    n -= 1
```
2. continue - pomijamy aktualną iterację i przechodzimy do kolejnej, np.
```
for i in range(11):
    print("I: ", i, "Potęga: ", 2 ** i)
    if i == 5:
        continue
    print("--- --- --- --- --- --- ---")
```

## Lista dynamiczna/składana

Ten kod:
```
numbers_v2 = [i for i in range(11)]
print(numbers_v2)
```
jest równoważny z:
```
numbers = []
for i in range(11):
    numbers.append(i)
print(numbers)
```

16.03.2023 - przejrzeć materiały z prezentacji do slajdu 89 (bez działu: operacje na plikach i programowanie obiektowe)

## Formatowanie STR
f"" (fprint) można wykorzystywać nie tylko w princie, ale równierz w tworzeniu zmiennych
```
print(f"Moje i równa się {i}, a potęga 2^i to: {2 ** i}")
```
Informacje z zewnątrz zmaieszczamy w klamrach. ważne jest wstawienie f przed "".

Powstawanie dziwnych reszt przy działaniach na wartościach (float) wynikają z dokładności binarnej. Dlatego python nie
utrzymuje perfekcyjnej dokładności danych.

Zakresy:
integer: do 255 (np. 300 zapisywane jest jako suma dwóch elementów) Dlatego duże liczby pomimo tej samej wartości ma
różne wartości. Dlatego dla a = 300 i b = 300, a is b zwróci false