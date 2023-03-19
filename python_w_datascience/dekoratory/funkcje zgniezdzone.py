# Przyklad zagniezdzenia funkcji w funkcji:
# def say_hi(name: str) -> None:
#     print(f"Hello, {name}")
#
# def get_name(say_hi) -> None:
#     return say_hi("Agnieszka")
#
# print(get_name(say_hi))
# Przykład nr 2:
# def parent():
#     def first():
#         print("First")
#
#     def second():
#         print("Second")
#
#     first()
#     second()
#     return first
#
#
# print(parent())
# Przykład nr 3:
def trigger_info(func):
    def wrapper(*args, **kwargs):   # Przekazanie arg do funkcji
        print(f"Wywołano funkcję {func}")
        return func(*args, **kwargs)       # Zwrócenie wartości przez funkcje
    return wrapper


@trigger_info
def my_add(a: float, b: float) -> float:
    return a + b


@trigger_info
def my_sub(a: float, b: float) -> float:
    return a - b

print(my_sub(10, 2))
print(my_add(10, 2))