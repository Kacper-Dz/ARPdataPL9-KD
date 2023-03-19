# Napisz funkcje, która jako pierwszy argument przyjmuje rodzaj operacji
# suma, róznica, iloczyn
# a nastepnie wykona sumowanie/dzielenie/mnożenie wszytskich argumentów
# podanych po pierwszym. Ilość argumentów do obliczeń może być dowolna.

def calculator(action: str, *args):
    if len(args) >= 2:
        result = args[0]
        if action == "add":
            for i in range(1, len(args)):
                result += args[i]
        if action == "multiply":
            for i in range(1, len(args)):
                result *= args[i]
        if action == "substract":
            for i in range(1, len(args)):
                result -= args[i]
        return result
    else:
        print(f"Podano za mało liczb")
        return args[0]


print(calculator("add", 1, 2, 3))
print(calculator("multiply", 1, 2, 3))
print(calculator("substract", 1, 2, 3))