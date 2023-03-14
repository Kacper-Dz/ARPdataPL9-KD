# Napisz funkcje o nazwie show_temp_status, która przyjmuje jeden argument typu float
# Nastepnie zwraca str (nie wykonuje print!) zależnie od wartości podanego argumentu:
#   Poniżej 36.4 - wychłodzenie
#   <36.4 36.8> - norma
#   <36.9, 37.0> - stan podgoraczkowy
#   Powyżej 3.71 - gorączka

def show_temp_status(temp):
    if temp < 36.4:
        return "wychlodzenie"
    elif 36.4 <= temp <= 36.8:
        return "norma"
    elif 36.9 <= temp <= 37.0:
        return "stan podgorączkowy"
    elif temp >= 37.1:
        return "gorączka"
