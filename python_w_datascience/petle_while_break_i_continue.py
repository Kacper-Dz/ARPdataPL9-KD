# n = 0
# while n < 10:
#     print(n ** 2)
#     n += 1

for i in range(11):
    print("I: ", i, "Potęga: ", 2 ** i)
    if i == 5:
        continue
    print("--- --- --- --- --- --- ---")

n = 10
while n > 0:
    if n == 4:
        break
    print("n=", n)
    n -= 1

# Lista dynamiczna
numbers = []
for i in range(11):
    numbers.append(i)
print(numbers)
# ==
numbers_v2 = [i for i in range(11)]
print(numbers_v2)

# ciekawostka - słownik składany
power_for_2 = {i + 1: 2**i for i in range(11)}
print(power_for_2)