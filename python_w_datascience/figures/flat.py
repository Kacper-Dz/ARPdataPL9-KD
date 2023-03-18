def rectangle_area(edge_a: float, edge_b: float) -> float:
    return edge_a * edge_b


def rectangle_circuit(edge_a: float, edge_b: float) -> float:
    return (2 * edge_a) + (2 * edge_b)


def is_square(edge_a: float, edge_b: float) -> bool:
    return edge_a == edge_b


def circle_circuit(radius_r: float) -> float:
    return 2 * radius_r * 3.14


def circuit_area(radius_r: float) -> float:
    return (radius_r ** 2) * 3.14
