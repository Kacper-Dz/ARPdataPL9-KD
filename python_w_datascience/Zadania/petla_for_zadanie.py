# Mamy listę danych:
data = [
    ("Adam", 750),
    ("Ewa", 250),
    ("Jakub", 200),
    ("Elżbieta", 1000),
    ("Adam", 400),
    ("Ewa", 300),
    ("Maja", 0)
]
# Nalezy przepisać powyższe krotki do słownika danych według poniższego schematu:
# klucz - 1 wartość krotki
# wartość - 2 wartość krotki podzielona przez 50
wynik: dict = {}
for i in range(0, len(data)):
    if data[i][0] not in wynik.keys():
        wynik[data[i][0]] = data[i][1]/50
print(wynik)
# Przykłądowo dla pierwszego elementu listy powinniśmy otrzymać wpis:
# "Adam": 15
#
# Program ma pomijac klucze, które sa duplikowane (wchodzi pierwsze wystąpienie) czyli
# drugi "Adam" powinien być pominiety w przetwarzaniu.
