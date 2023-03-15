# Mamy listę danych:
data = [
    ("Adam", 750),
    ("Ewa", 250),
    ("Jakub", 200),
    ("Elżbieta", 1000),
    ("Adam", 400),
    ("Ewa", 300)
]
# Nalezy przepisać powyższe krotki do słownika danych według poniższego schematu:
# klucz - 1 wartość krotki
# wartość - 2 wartość krotki podzielona przez 50
#
# Przykłądowo dla pierwszego elementu listy powinniśmy otrzymać wpis:
# "Adam": 15
#
# Program ma pomijac klucze, które sa duplikowane (wchodzi pierwsze wystąpienie) czyli
# drugi "Adam" powinien być pominiety w przetwarzaniu.