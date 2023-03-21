# Znak nowej linii: /n
# Przykładowy problem, wyświetli imię i jego długość
# print(file.read(0))      Czyta określoną ilość znaków albo wszystkie
# print(file.readline(0))  Czyta do znaku nowej linii
# print(file.readlines())  Zapisuje sczytane linie do listy

with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        tmp = line.replace('\n', '')  # Pozbycie się \n, ponieważ python nie pozwala na użycie \n w princie
        print(f"{tmp} - {len(tmp)}")
    print(file.readline())
