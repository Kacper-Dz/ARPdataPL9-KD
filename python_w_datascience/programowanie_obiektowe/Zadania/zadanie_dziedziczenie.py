# Napisać klasę Person, która zawiera pola:
#       - imie (str)
#       - nazwisko (str)
#       - adres (str)
#       - wiek (int)
# Dodatkowo klasa posiada metody:
#       - __str__ - zwraca tekst w formacie: "Nazwiska, Imie, Adres"
#       - check_is_adult - zwraca true, jeżeli wiek >= 18

# Napisać klasę Customer, która dziedziczy po Person, a dodatkowo posiada pola:
#       - orders (list)
#       - login (str)
#       - total_order_cost (float)
# Oraz funkcje:
#   - str- wykorzystuje odziedziczony str, a dodatkowo na początku podaje login
#   - add_order(product, cost) - dodaje krotke do listy zamówień
#       Można dodac zamówienie tylko jak użytkownik jest pełnoletni
#       Dodatkowo aktualizuje wartość total_order_cost po dodaniu zamówienia
#    - show_orders() - wyśweitla wszytskie zamówienia

class Person:
    def __init__(self, imie, nazwisko, adres, wiek):
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.adres: str = adres
        self.wiek: int = wiek
        self.pelno: bool = False

    def __str__(self):
        return f"{self.nazwisko}, {self.imie}, {self.adres}"

    def adult(self):
        return self.wiek >= 18


class Customer(Person):
    def __init__(self, imie, nazwisko, adres, wiek, orders, login, total_order_cost):   # Alternatywnie, deklarujemy bez total_order_cost i orders - nie wymagają deklaracji przy tworzeniu elementu
        super().__init__(imie, nazwisko, adres, wiek)
        self.orders: list = orders
        self.login: str = login
        self.total_order_cost: float = total_order_cost

    def __str__(self):
        return f"{self.login}, {super().__str__()}"

    def add_order(self, product, cost):
        if super().adult():
            self.orders.append((product, cost))
            self.total_order_cost += cost
        else:
            print(f"Użytkownik {self.login} nie jest pełnoletni")

    def show_orders(self):
        print(self.orders)


c1 = Customer("Jan", "Kiepura", "Topolowa", 18, [], "marycha2", 45)
print(c1.adult())
c1.add_order("Ziemniaki", 50)
c1.show_orders()
