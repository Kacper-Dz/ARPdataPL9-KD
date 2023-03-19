# Napisać dekorator dla funkcji, która nie przyjmuje argumentów oraz niczego nie zwraca, którego zadaniem jest
# wyświetlenie po wywołaniu funkcji napisu "---Koniec---"

def line_finisher(func):
    def wrapper():
        func()
        print(f"--- KONIEC ---")
    return wrapper


@line_finisher
def powitanie() -> None:
    print(f"Hello")


powitanie()
