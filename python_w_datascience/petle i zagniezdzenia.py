# Lista krotek
accounts = [
    ("A001", "234876", 250.60),
    ("B002", "200123", 45.76),
    ("A003", "456321", 1234.67)
]
# Dla przykładu powyżej:
#           0       1       2
#   0   [0][0]  [0][1]  [0][2]
#   1   [1][0]  [1][1]  [1][2]
#   2   [2][0]  [2][1]  [2][2]


# # Do poczytania: listy zagnieżdżone
#
# print(accounts)
# print(accounts[-1])  # Zwraca krotkę [-1] (ostatni element listy)
# print(accounts[-1][2])  # Zwraca wartość [2] w krotce [-1]
# print(accounts[0][2], accounts[1][2])
#
# # Pętle for
# # 1. Łańcuch znakowy:
# for c in "KOTEK":
#     print("Litera: ", c)
#
# 2. Łańcuch znakowy -> lista
# for word  in "Ala ma kota".split(" "):
#     print("Słowo: ", word)
#
# 3. lista/krotka
# for element in accounts:
#     print("Klient: ", element)
#
# 4. Sekwencja liczb (range) - generuje zakres liczb na podstawie danego ciągu
# range(start, end, step) | <start, end-1>
# Domyślnie krok =1
# Range(10) - <0,9>
# Range (1,12) - <1,11>
# Range (2,10,2) - <2,9> z krokiem 2
# for i in range(2, 10, 2):
#     print("Liczba:", i)
# 4a. Ciąg malejący, od 11 do 0
for i in range (11, -1, -1):
    print(i)