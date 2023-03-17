# Zadanie 01
# Napisać funkcję, która zamienić stopnie Celsjusza na Kelwina. Funkcja przyjmuje jako argument temperaturę w C,
# a funkcja zwraca temperaturę w K. Obie wartości maja być typu float

def temp_conversion(cels: float):
    return float(cels + 273.15)

# Zadanie 02
# Napisać funkcję, która jako argument przyjmuje dowolny łańcuch znakowy, a następnie zwraca słownik zliczający ilość
# wystąpień każdego słowa (kot =/= kota). Podpowiedź możemy użyć metody ```split(" ")```.

def word_count(text):
    count = {}
    word = text.split(" ")
    for c in word:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    return count


ciag = "Ala ma kota a kot ma pierdolca"
print(word_count(ciag))

# Zadanie 03
# Użytkownik podaje trzy liczby całkowite. Następnie program zwraca informację, która z podanych liczb jest największa
# (dla odważnych - możecie również weryfikować czy dane liczbą są takie same).

# numbers = [float(input("Podaj pierwszą liczbę: ")),
#            float(input("Podaj drugą liczbę: ")),
#            float(input("Podaj trzecią liczbę: "))]
# # print("Największa liczba z podanych to:", max(numbers))
# maxi = 0
# for i in numbers:
#     if i > maxi:
#         maxi = i
# print("Największa licza z podanych wynosi:", maxi)

# Wersja z weryfikacja licz
numbers = [float(input("Podaj pierwszą liczbę: "))]
num2 = float(input("Podaj drugą liczbę: "))
while num2 == numbers[0]:
    num2 = float(input("Podana liczba jest taka sama ja poprzednia, podaj inną liczbę: "))
else:
    numbers.append(num2)
num3 = float(input("Podaj trzecią liczbę: "))
while num3 == numbers[0] or num3 == numbers[1]:
    num3 = float(input("Podana trzecia liczba jest podobna do poprzednio podanych, podaj inną liczbę: "))
else:
    numbers.append(num3)

maxi = 0
for i in numbers:
    if i > maxi:
        maxi = i
print("Największa licza z podanych wynosi:", maxi)

# Zadanie 04
# Napisać program, gdzie użytkownik podaje liczby całkowite i je sumuje. Program działa dopóki użytkownik nie poda
# liczby ujemnej. Po podaniu liczby ujemnej program wyświetla sumę podanych poprzednich liczb.

liczba = int(input("Podaj pierwszą liczbę do zsumowania: "))
suma = liczba
while liczba >= 0:
    liczba = int(input("Podaj kolejną liczbę do zsumowania: "))
    suma += liczba
else:
    print("Podana liczba jest ujemna! Suma podanych wcześniej liczb wynosi: ", suma - liczba)

# Zadanie 05
# Napisać funkcję, która konwertuje liczbę z systemu dziesiętnego na binarny
# (nie używamy funkcji wbudowanych w Pythonie)

def dzie_to_binar(dzies):
    reszta = ""
    while dzies > 0:
        reszta = str(dzies % 2) + reszta
        dzies = dzies // 2
    return reszta

liczba = int(input("Podaj liczbę, która zostanie zamieniona na system dziesiętny: " ))
print(dzie_to_binar(liczba))


# Zadanie 06
# Użytkownik podaje liczbe całkowitą. Następnie program zwraca sumę CYFR z których składa się podana liczba.
# Przykładowo: użytkownik podaje 1307, program zwraca 11 (1+3+0+7). Podpowiedź: konwersja na str

liczba = str(input("Podaj liczbe całkowitą: "))
suma = 0
for i in liczba:
    suma += int(i)
print(suma)

# Zadanie 07
# Napisać program, gdzie użytkownik podaje n łańcuchów znakowych (ilość n również definiuje wcześniej użytkownik).
# Następnie program zwraca informacje ile łańcuchów znakowych jest unikatowych. :)
# Przykładowo: użytkownik podał n = 3. Następnie podał trzy łańcuchy znakowe: ```Kot```, ```Pies```, ```Kot```.
# Program zwróci informacje, że ilość UNIKATOWYCH łańuchów znakowych to: 2.

ilosc = int(input("Ilość łańcuchów znakowych do wprowadzenia: "))
lista = []
for i in range(ilosc):
    lista.append(input(f"Podaj ciąg znaków nr {i+1}:  "))
unikat = []
for c in lista:
    if lista.count(c) <= 1:
        unikat.append(c)
print("Ilość unikatowych łańcuchów to:", len(unikat))