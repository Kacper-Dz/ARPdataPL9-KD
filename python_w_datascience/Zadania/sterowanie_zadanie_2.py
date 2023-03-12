# Użytkownik podaje liczbę, a następnie program:
liczba = int(input("Podaj proszę liczbę: "))
# Wyswietli "Pif paf", jezeli podana liczba jest podzielna przez 3  i 5
if liczba % 3 == 0 and liczba % 5 == 0:
    print("Pif! Paf!")
# Wyswietli "Pif", jezeli podana liczba jest podzielna tylko przez 3
elif liczba % 3 == 0:
    print("Pif!")
# Wyswietli "Paf", jezeli podana liczba jest podzielna tylko przez 5
elif liczba % 5 == 0:
    print("Paf!")
# Wyswietli komunikat "Twoja liczba to: " + podana liczba, jeżeli nie spełniono żadnego z warunków
else:
    print("Twoja liczba to:", liczba)
