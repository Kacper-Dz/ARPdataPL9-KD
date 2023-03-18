def my_add (num_a: float, num_b: float) -> str:
    return str(num_a + num_b)


def my_sub (num_a: float, num_b: float) -> str:
    return str(num_a - num_b)


def my_div (num_a: float, num_b: float) -> str:
    if num_b != 0:
        return str(num_a / num_b):
    else:
        return "Nie można dzielić przez zero!"
