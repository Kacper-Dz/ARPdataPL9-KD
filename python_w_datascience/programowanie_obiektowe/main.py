class Car:
    def __init__(self, color, price, brand):
        self.color = color
        self.price = price
        self.brand = brand
        self.running = False
        self.spec = []

    def __str__(self):
        return f"{self.brand}, {self.color}, {self.price}"

    def __float__(self):
        return self.price

    def switch(self):
        if self.running:            # Jeżeli self.running ma wartość true, wtedy:
            self.running = False
        else:                       # Jeżeli self.running nie jest true, wtedy:
            self.running = True


c1 = Car("Czerwony", 4500000, "Ferrari")
c2 = Car("Zielony", 20000, "Opel")

print(c1.color, c2.color)
print(c1.running, c2.running)
c1.switch()
print(c1.running)
print(c1)
