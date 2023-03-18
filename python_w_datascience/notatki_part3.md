# Python w Data Science - part 3
## Formatowanie
* fprint jako zaokraglenie liczb zmiennoprzecinkowych (formatowanie)
```
print(f"Wartość: {value:6.2F}") # value zajmuje 6 miejsc (z kropką), z czego 2 po przecinku
```
*f - miejsca po przecinku
*d - ilość znaków dla int

## Moduły

Moduły dostarczają funkcji do kodu, np. moduł math:
```
from math import sqrt

print(sqrt(4))
```
ctrl + spacja - okno podpowiedzi w pycharmie, ikony folderów z kropką oznaczają pakiety, które dostarcza większą 
`funkcjonalność niz sam folder

Możemy importować wybiórczo albo całość, np. import math ale jest to mocno niezalecane

Aliasowanie własnych modułów:
```
from FOLDER.KOLEJNYFOLDER.Plik import FUNKCJA as NAZWAFUNKCJI
```
- Bardzo ważne jest aby nazwy katalogów były z pojedynczych nazw!!! metoda KIS - keep it simple stupid
- __init__.py - tworzy onfo, że dany folder jest pakietem
- Nazwy folderów nie mogą się zaczynać od cyfry
- Daty warto umieszczać na końcu
- Nalezy pamietac o odpowiednim importowaniu modułów, jeżeli w module B używamy modułu A, w main musimy zaimportować
  modul A i B, nie działa to kaskadowo
- Staramy się, żeby moduły nie były od siebie zależne!!!
- Moduł jest niezależny od innych

## Nazewnictwo

- Funkcje: ```len(x)```, ```print(x)```
- Metody: To funkcje wybranej klasy/wartości np. ```l.append(y)```, ```txt.lower()```, ```d.get(x, y)```
- Atrybuty/Pole: To zmienne należące do klasy (czyli takie które definiujemy z użyciem ```self```)
- Argument == Parametr
- Wartość: informacja, którą można zapisać np. do zmiennej

## Obiekty

W przypadku programowania biektowe musimy zdefinować schemat(klasę) dla danego obiektu. Klasa będzie nam opisywac czym
jest sam w sobie obiekt.

* nazwy klas piszemy od dużej litery:
```
class Car:
```
* Nazwa __nazwa__ to jest tzw. magic function:
```
def __init__(self, color, price, brand):
```
* Są to funkcje, które są wykonywane nawet jesli nie ma ich w kodzie i są wykonywane w odpowiednim momencie. __init__ 
  pozwala na definicje zmiennych atrybutów, które będziemy używać w danej klasie.
```
        self.color = color
        self.price = price
        self.brand = brand   
```
Dzięki temu można odróżnić co przychodzi z zewnątrz a co jest w ramach danej klasy (self.nazwa)

- Obiekt tworzymy przez wywolanie klasy podając paramtery i możemy potem wywołać poszczególne elementy tej klasy:
```
c1 = Car("Czerwony", 4500000, "Ferrari")
c2 = Car("Zielony", 20000, "Opel")

print(c1.color, c2.color)
```
- podawanie zmiennej przez uzytkownika jest zawsze poza obiektami/funkcjami.
- Przywoływanie funkcji i zmiennych wenwątrz danej klasy odbywa się z wykrozystanie przedrostka ```self.XXXXX```
- Dla zdefiniowanej klasy możemy określic zwracany łancuch znakowy, np. dla funkcji print:
```
    def __str__(self):
        return f"{self.brand}, {self.color}, {self.price}"
```
- albo dla float:
```
    def __float__(self):
        return self.price
```
- zmiana przypisanego atrybutu:
```
obiekt.atrybut = "Nowa wartość atrybutu"
```
## Dziedziczenie

- Można stworzyć nową klasę, która dziedziczy atrybuty po poprzedniej (superclass).
- alt + shift + enter (add super class call) - autouzupełnienie odwołania do super klasy.
- Odwołanie się do klasy dziedziczonej:
```
super().__init__(legs_count, eyes_count, name)
```
- Dziedziczenie obowiązuje cały zestaw atrybutów.
- Dziedziczone są także aktrybuty zdefiniowane domyślnie.
- Jeżeli super klasa i klasa mają sdefiniowane __str__ to domyslnie działa str dla klasy.
- Odniesienie sie np. do str w klasie super:
```
super().__str__()
```