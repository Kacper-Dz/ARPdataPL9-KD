class Employee:
    def __init__(self, fname: str, lname: str, age: int) -> None:
        self.fname = fname
        self.lname = lname
        self.__age = age
    #getter

    @property
    def age(self):
        return self.__age

    # Setter
    @age.setter
    def age(self, new_age):
        self.__age = new_age

p1 = Employee("Jan", "Kowalski", 30)
# Te dane sa dostepne w pamieci bezposredniej, sa podatne na ataki, aby utworzyc zmienna prywatna/zabezpieczona to
# należy użyć __, np. self.__age - nie bedziemy mieli do niego bezpośredniego dostępu
print(p1.age)
p1.f_name = "Adam"
print(p1.f_name)
p1.age = 42
