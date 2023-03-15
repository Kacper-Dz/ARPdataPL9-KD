# Python w Data Science

## Podstawowe informacje

Plik - podstawy.py
W pythonie używamy małych liter.

Typy danych:

* str - łańcuch znakowy; txt = "Ala ma kota"
* int - liczby całkowite; number = 12
* bool - logiczny (prawda/fałsz); num_with_precision = 9.99
* float - liczby z precyzją; true_or_false = True

Wyświetlanie danych; print()

Czy używać zmiennej czy bezpośrednio prowadzić obliczenia:
Czy będę jeszcze korzystał z tej zmiennej/wykorzystywał ją w dalszych obliczeniach?

Operacje na wartościach
Konkatencaja tesktu - dodawanie tekstu
Potęgowanie; **
Reszta z dzielenia; % - python modulo
Dzielenie bez reszty; //

skrócony zapis
x = x ** 2 to to samo co x ** = 2
y = y - 1  => y -= 1
x = x ** 10 => x ** =10

ctr + / - zakomentowanie/odkomentowanie kodu dla danego zaznazczenia

Zmienne użytkownika:
funkcja; zmienna_którą_chcę_wprowadzić = input("tu może być przykładowy teskt")

Input zapisuje wprowadzone dane jako dane tekstowe!!!
print(type(zmienna)) - weryfikacja typu zmiennej

Format typ_danych(liczba/zmienna do konwersji:
str(), int(), float(), bool()

Konwersja może prowadzić do utraty danych np z 9.99999 robi 9
Python rozpozna 9 jako int() a 9.0 jako float()
print(pierwsza komenda, druga komenda, trzecia komenda)

Funkcja voight/noun - funkcje po wykonaniu nie zwracają żadnej wartości
## Pętle
```
if 'warunek' :
    # co jeśli 'warunek' jest spełniony
else:
    # co jeśli 'warunek' nie jest spęłniony
```
not- negacja
or - 0 lub 1 daje 1
and - 1 i 1 daje 1

'==' porównanie warunków

W1 and W2 or W3
1. Najpierw sprawdzane jest W1 and W2, jesli true
2. Sprawdzanie jest z W3 

Można łączyć warunki, np: 2 <= x <= 5, to samo co x >= 2 and x <= 5

elif - sprawdzenie kolejnego warunku, jesli poprzedni nie był prawdziwy
Przy wielu elif'ach pętla działa do pierwszego spełnienia elif
## Funkcje
def [nazwa funkcji] (argumenty funkcji, jeśli brak - pusty nawias):
Funkcje niczego nie zwracają, wykonują tylko określone zadanie.
Jeżeli funkcja ma coś zwrócić, należy użyć polecenia 'return'

Książka prowadzona za rękę: Python dla każdego, podstawy programowania

## Kolekcje danych

txt = "Ala ma kota."

Warunek na podstawie zbioru
```
if "pies" in txt:
    print("Ala faktycznie ma kota")
```
len() - podanie długości danego tekstu

print(txt.upper()) - na txt działamy metodą upper()

https://www.w3schools.com/python/python_ref_string.asp
https://docs.python.org/3/library/stdtypes.html
https://www.programiz.com/python-programming/methods/string

Dokumentacja jest naszym przyjacielem.

## Listy

Można mieszać listy, można np umieścić listę w liscie.
Najlepiej trzymać się jednego typu danych w ramach listy, choć technicznie można zamieścić kilka
typów, aczkowliek nie jest to zalecane.

Pusta lista: 

```empty = [] lub empty = list()```

Funkcje agregujące i działania na listach: 

```
- sum(lista) - suma
- max(lista) - maximum
- min(lista) - minimum
- .clear() - wyczyszczenie listy
- .append() - dodanie nowego elementu do listy
- .extend() - roszerzenie listy o wiele elementów (podajemy jako liste)
- .index() - podaje index szukanego elementu
- .insert() - pozwoli dodać element pod dodanym indexem, jezeli istnieje el. pod danym
   indexem -> lista zostanie rpzesunięta w prawo
- .remove() - usuwanie wybranego elementu z listy, pierwszego napotkanego od poczatku/lewej strony. Działa tak długo jak
   dostępne są wartości tego typu
- .pop() - usuwanie wskazanego elementu po wskazanym indeksie, jeśli nie jest wskazany - usuwa ostatni, pierwszy po 
   prawej - zwraca tez usunieta wartosc
```
Unikamy używania funkcji input w funkcjach

## Słownik

Słownik, tablica asocjacyjna - łączy klucz z wartością. Podobnie działa jak lista. Różnica polega na tym, że w przypadku
słownika sami definiujemu klucz. Słownik definujemy w klamrach {}.

```
contacts = {
    "Adam":"670234515",
    "Ewelina":"123456745",
    "Piotr":"000235423"
}
```
Sprawdzenie, czy istnieje klucz:
```
if "Iza" in contacts.keys():
    print("Kontakt istnieje.")
```
Klucze w słowniku, tak jak indesky w liście, musza być unikatowe.

.get("Nazwa klucza") -> zwraca wartość klucza = nazwa_słownika["Nazwa klucza"]
.get("Nazwa klucza", Wartość do zwrócenia jeśli podany klucz nie istnieje)

2 opcje na rozwiązanie problemu z brakiem klucza:
```
# 1
print(contacts.get("Bożydar", -1)

# 2
if "Bożydar" in contact.keys():
    print(contacts["Bożydar"])
else:
    print(-1)
```
Usuwanie - funkcja .pop() - musimy podać argument do usunięcia, na pusto nie zadziała.
## Przepisywanie pod nowy klucz
```
contacts["Mateusz"] = contacts.pop("Ewelina")
```
## Typowanie danych
Typowanie zwieksza higienie kodu.
```
# Przykład:
def add_contacts(contacts: dict, name: str, phone_nr: str) -> None:
# zmienna: [typ zmiennej]
# -> None:  # To jest informacja o tym jaki typ danej jest zwracany przez funkcję
```
Zastosowanie tego zwiększa higienę kodu, jest to podpowiedź dla programu pod kątem proponowanych funkcji.

## Krotka (tuple)

W krotce nie można zmieniać wartości, jest niemutowalna. Działa jak lista, definiujemy ją za pomocą 
nawiasów otwartych (). Wpisane wartości mogą się powtarzać. Nie ma narzędzi do jej edycji. Jedyna możliwość 
jej edycji to ponowne jej nadpisanie. Zastosowanie krtoki jest gwarancją, że dane nie ulegną zmianie w trakcie
procesowania.

## Zbiór

Definicja pustego zbioru odbywa się za pomocą (), jeżeli użyjemy {} to python zinterpretuje to jako
pusty słownik. Definicja zbioru:
```
numbers ={1, 2, 3, 4, 5, 6, 7, 1, 4, 6}
# Pusty zbiór: n =set()
```
Zbiór przechowuje wartości unikalne, które są posortowane. Nie mamy gwarancji stałej 
kolejności elementów. Pozwala na ekonomizajację użycia pamięci w poszukiwaniu unikalnych elementów.

## Zagnieżdżenia

Lista krotek
```
accounts = [
    ("A001", "234876", 250.60),
    ("B002", "200123", 45.76),
    ("A003", "456321", 1234.67)
]
```

## Pętle - część kolejna
Pętla for działa tak długo, jak mamy dane w zbiorze. Tzn. wykona się dla każdego znaku w łańcuchu.
1. Łańcuch znakowy:
i - dla liczb, c - dla tesktu
```
for c in "KOTEK":
    print("Litera: ", c)
```
Da wynik:
```
Litera:  K
Litera:  O
Litera:  T
Litera:  E
Litera:  K
```
