# Warunki atytmetyczne
# x = 3
# if x >= 3:
#     print("Jebać to, nie kupuj cebuli!!!")
# else:
#     print("Czysta cebula! Kup od razu trzy!")
# Operatory: not, and, or
# cost = 3
# product = "cebula"
# if product == "cebula" and cost < 3:
#     print("Czysta cebula! Kup od razu trzy!")
# else:
#     print("Nie tykaj bo śmierdzi Januszerką!")
# # Operator in/not in (później) oraz przedziały
# grade = 4.7
# if 2 <= grade <= 5:
#     print("Ocena prawidłowa")
# else:
#     print("Ocena nieprawidłowa")
#
# elif - sprawdza kolejny warunek, jak poprzedni był nieprawdziwy
cost = 3.10
product = "cebula"
if product == "cebula" and cost <= 3:
    print("Kupujesz cebulę!")
elif product == "marchewka" and cost <= 4.5:
    print("Kupujesz marchewkę!")
elif product == "wódka" and cost <= 19.99:
    print("Kupujesz alkohol!")
else:
    print("Wychodzisz bez zakupów!")
