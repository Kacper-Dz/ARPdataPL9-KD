# Napisz klasę o nazwie Product, która zawiera pole:
#       - nazwa (str)
#       - kategoria (str)
#       - sn (str)
#       - price (float)
# Zmienne sn oraz price są prywatne a dostep do nich jest możliwy dzięki getter/setter
# Dodatkowo nie można ustawić price mniejsza niż 0.01. Każda próba ustawienia wartości mniejszej niż 0.01
# powoduje ustawinie 0.01)

class Product:
    def __init__(self, name, category, sn, price):
        self.name = name
        self.category = category
        self.__sn = sn
        self.__price = price

    @property
    def price(self):
        return self.__price

    @property
    def sn(self):
        return self.__sn

    @sn.setter
    def sn(self, sn_set):
        self.__sn = sn_set

    @price.setter
    def price(self, new_price):
        if new_price >= 0.01:
            self.__price = new_price
        else:
            self.__price = 0.01


p1 = Product("intel i7", "CPU", "000-000-0001", 5300.00)
p1.price = -2
print(p1.price)