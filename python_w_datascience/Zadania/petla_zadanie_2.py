# Napisz funkcję, która przyjmuje łańcuch znakowy (dla ułatwienia: same małe litery)
# Przykładowo: alamakotaakotmapierdolca
# Funkcja ma zwrócić słownik (return), który zawiera informacje w postaci:
#       Klucz - litera
#       Wartość - ilość wystapień litery w tekście
# Przykładowo: dla klucza "l" wartość to 2


def count_letters(text: str) -> dict:
    result = {}
    for c in text:
        if c not in result.keys():
            result[c] = 1
        else:
            result[c] += 1
    return result


lista = "alamakotaakotmapierdolca"
print(count_letters(lista))


# Alternatywna forma
def char_counter(text: str) -> dict:
    result = {}
    for c in text:
        if c not in result.keys():
            result[c] = text.count(c)

    return result


print(char_counter(lista))

