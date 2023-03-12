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
# Pętle
if 'warunek' :
    co jeśli 'warunek' jest spełniony
else:
    co jeśli 'warunek' nie jest spęłniony

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
# Funkcje
def [nazwa funkcji](argumenty funkcji, jeśli brak - pusty nawias):
Funkcje niczego nie zwracają, wykonują tylko określone zadanie.
Jeżeli funkcja ma coś zwrócić, należy użyć polecenia 'return'