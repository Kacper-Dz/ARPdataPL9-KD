# Użytkownik podaje ilość losowań (n), a nastepnie program zapisuje do pliku n przykładowych wyników lotto
# Przykład, użytkownik podaje n = 2
# * pomijaj duplikaty
# Wynik (zawartość pliku):
# 2 6 12 40 31 22
# 12 34 49 21 1 12
from random import randint
n = int(input("Podaj ilość losowań: "))
tmp = []
x = 0
with open("lotto.txt", "w+", encoding="utf-8") as file:
    for i in range(n):
        for c in range(6):
            while len(tmp) < 6:
                x = randint(1, 49)
                if x not in file:
                    tmp.append(f"{x} ")
        file.writelines(tmp)
        file.write("\n")
        tmp = []
with open("lotto.txt", "r", encoding="utf-8") as file1:
    print(file1.readlines())

# alternatywa - ta lepsza
v = int(input("Podaj ilość losowań: "))
for i in range(v):
    numbers = set()
    while len(numbers) < 6:
        numbers.add(f"{randint(1, 49)} ")

    with open("lotto.txt", "a+", encoding="utf-8") as file2:
        file2.writelines(numbers)
        file2.write("\n")
