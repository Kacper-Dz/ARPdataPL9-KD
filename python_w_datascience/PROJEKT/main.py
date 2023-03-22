from datetime import datetime as dt, timedelta as td
from random import randint, uniform

rows_count = 10
for i in range(rows_count):
    tmp_row = []
    now = dt.now() + td(hours=randint(-24, 24)) + td(minutes=randint(-60, 60))
    tmp_row.append(f"{now.strftime('%H:%M')};{randint(0, 100)};{round(uniform(0.1, 1.0), 1)}\n")
    with open("dane_dzienmiesiacrok.txt", "w+", encoding="utf-8") as file:
        file.writelines(tmp_row)

# Przykladowe rozwiazanie:

# from datetime import datetime as dt, timedelta as td
# from random import randint, uniform

for i in range(0):
    with open("test_data.txt", "a", encoding="utf-8") as file1:
        time = dt.now() - td(hours=randint(-24, 24), minutes=randint(-60, 60))
        first_value = str(randint(0, 100))
        second_value = str(round(uniform(0.1, 1.0), 2))
        row = time.strftime("%H:%M") + ";" + first_value + ";" + second_value + "\n"
        file1.write(row)

# Przykład optymalizacyjny - ograniczmy ilość procesów otwierania i zamykania pliku:

for c in range(10):
    with open("test_data.txt", "a", encoding="utf-8") as file1:
        for i in range(100000):
            time = dt.now() - td(hours=randint(-24, 24), minutes=randint(-60, 60))
            first_value = str(randint(0, 100))
            second_value = str(round(uniform(0.1, 1.0), 2))
            row = time.strftime("%H:%M") + ";" + first_value + ";" + second_value + "\n"
            file1.write(row)
