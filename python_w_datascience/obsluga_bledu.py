# x = 10
# try:
#     print( x / 1)
# except ZeroDivisionError: # except: <-- instrukcje dla wystąpienia dowolnego błędu, unikamy obsługi wszytski kodów błędu na raz
#     print("Próbowałeś/aś dzielić przez zero.")
#
# a = [10, 34, 24, 5, "ala ma kota", True, 3, 5, 6, "piesek", "xD", 20]
# errors_value = []
# for i in range(len(a)):
#     try:
#         a[i] = a[i] + 2
#     except TypeError:
#         errors_value.append(a[i])
#
# print(errors_value)
# print(a)

try:
    print(10/0)
    print("Ala ma " + 5 + "kotów.")
except ZeroDivisionError:
    print("Próbowano dzielic przez zero")
except TypeError:
    print("Wystąpił problem z typem danych.")