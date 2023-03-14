# Program przyjmuje od użytkownika dwie liczby:
#   1. Liczba prawidłowych odpowiedzi (int)
#   2. Liczba pytań (int)
pyt = int(input("Podaj całkowitą ilość pytań: "))
odp = int(input("Podaj proszę ilość prawidłowych odpowiedzi: "))
# Nastepnie program wyświetla odpowiedni komunikat na konsoli zależnie od % prawidłowych odpowiedzi:
#   100% - 90% : 5.0; 89%-76% : 4.5; 75% - 70% : 4.0
#   69% - 60% : 3.5; 59% - 50% : 3.0; 49% - 0%: 2.0
proc = (odp / pyt) * 100
if 100 >= proc >= 90:
    print("Ocena: 5.0")
elif 89 >= proc >= 76:
    print("Ocena: 4.5")
elif 75 >= proc >= 70:
    print("Ocena: 4.0")
elif 69 >= proc >= 60:
    print("Ocena: 3.5")
elif 59 >= proc >= 50:
    print("Ocena: 3.0")
elif 49 >= proc >= 0:
    print("Ocena: 2.0")
else:
    print("Podane dane są nieprawidłowe!")
