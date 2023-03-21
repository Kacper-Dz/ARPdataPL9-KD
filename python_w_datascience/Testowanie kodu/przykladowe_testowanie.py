def show_temp_status(temp: float) -> str:
    try:
        if 36.7 <= temp < 36.8:
            return "OK"
        else:
            return "NOT OK"
    except TypeError:
        return "ERROR"


assert show_temp_status(36.6) == "NOT OK"
assert show_temp_status(30.0) == "NOT OK"
assert show_temp_status(40.0) == "NOT OK"
assert show_temp_status("Ala ma kota") == "ERROR"

def list_power(numbers: list) -> list:
    result = []
    for i in numbers:
        result.append(i ** 2)
    return result

assert list_power([1, 2, 3]) == [1, 4, 9]

