# Python w Data Science - part 4
## Operacje na plikach
## Odczyt
- Python szuka plików w miejscu, w którym się znajduje, wtedy wystarczy podać jego nazwę.
- Inaczej musimy podać "absolute path"
- Pod widnowsem musimy użyć podwójnych ```"C:\\Users\\Kacper\\Repositories\\ARPDATAPL9-KD\\python_w_datascience\\Praca na plikach\\names.txt"```
Komenda: 
```open(ścieżka, tryb otwarcia, encoding) as "nazwa zmiennej pod którą jest to dostępne``` 
Tryb otwarcia:
- ``r``   Open text file for reading.  The stream is positioned at the
         beginning of the file.
- ``r+``  Open for reading.  The stream is positioned at the
         end of the file.
- ``w``   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.
- ``w+``  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.
- ``a``  Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.
- ``a+``  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
Encoding:
- typ kodowania pliku
- domyślnie: "utf-8"

Przykładowo ```with open("names.txt", "a", encoding="utf-8") as file:```

- operacja na tym pliku działa jako np. ```file.read()```
- funkcja open odczytuje zawartosć całego pliku, nie rozróżnia nowych lini
- znak nowej lini: \n
- Przy poniższym kodzie przeczyta 14 znaków po kolei:
```
    print(file.read(7))
    print(file.read(7))
```
- w przypadków plików linia = tekst + \n
- ```read(n)``` - czyta n znaków
- ```readline(n)``` - czyta n znaków do n\ włącznie, po doczytanie \n kończy działanie
- ```readlines(n)``` - zapisuje pobrane linie do listy, 1 element = 1 linia + \n (jeśli dostępny), niezależnie od 
                       podanej ilości znaków zawsze zapisuje pełne linie
- W ten sposób nie ładuje całego pliku do pamięci, tylko na bieżąco odczytuje potrzebne elementy
## Zapis
- zapis danych odbywa sie w momencie zakonczeniu funkcji
- nie trzeba pamietac o zamknieciu pliku (zaleta funkcji with)
- normalnie byłoby
```
file = open()
file.write()
file.read()

file.close()
```
- rozwiązabie z ```with``` jest zdecydowanie bezpieczniejsza i wygodniejsza
- ```.writelines``` - przyjmuje krotke, zbior itp. (byle to bylo iterowalne) i każdy element krotki zapisuje jako 
   nową linię, każdy element musi mieć ```\n``` na końcu poza ostatnim
- w ramach jednego towrzenia możemy albo zapisać albo odczytać plik, nie możemy dwukrotnie tego samego zrobić

# Testowanie kodu
Dzielimy na 2 kategorie:
- weryfikacja (po naszej stronie)
- walidacja (po stronie klienta)

Rodzaje testów:
- funkcjonalne
- niefunkcjonalne/wydajnościowe
- pielęgnacyjne
Poziomy testów:
- integracyjne (test zgodności działania)
- jednostkowe (testy modułów)
- akceptacyjne/walidacyjne
- systemowe

Funkcja ```assert``` sprawdza działanie funkcji jako true or not true

