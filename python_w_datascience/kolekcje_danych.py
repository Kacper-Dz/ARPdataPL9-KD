# Łańcuch znakowy jako kolekcja danych

txt = "Ala ma kota."

# Warunek na podsatwie zbioru

# if "kot" in txt:
#     print("Ala faktycznie posiada kota.")
#
# print(len(txt))
# print(txt.upper())
# print(txt.lower())
# print(txt.isalnum())

# indeksowanie | 0...(len-1)
#                                               Po długości tekstu | Po numerze indeksu
print(txt[0])       # wyświetl 1 znak
print(txt[:4])      # wyświetl od 0 do 4;       <0,4) | <0, 3>
print(txt[2:8])     # wyświetl od 2 do 8;       <2,8) | <2,7>
print(txt[3:])      # wyświetl od 3 do końca;   <3, len> | <3, len-1>
print(txt[2:8:2])   # Co drugi znak od 2 do 7;  co drugi <2,7> - <2,4,6>    \
print(txt[::3])     # Dla <txt> wyświetlaj co trzeci znak                   |} zapis krokowy
print(txt[::1])     # Od końca                                              /

# Odwrócone indeksowanie
#   H   E   L   L   O
#   0   1   2   3   4
#   -5  -4  -3  -2  -1
