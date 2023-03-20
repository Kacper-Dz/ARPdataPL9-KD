def quadratic_func(a: float, b: float, c: float):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b - (delta ** 0.5)) / 2
        x2 = (-b + (delta ** 0.5)) / 2
        return x1, x2
    if delta == 0:
        x1 = -b / (2 * a)
        return x1
    if delta < 0:
        return None


def second_element(number: float) -> float:
    return number ** 0.5


def harmonic_func(element: int) -> float:
    return 1 / element
