# fprint jako zaokraglenie (formatowanie)
value = 3.9877773
print(f"Wartość: {value:6.2f}")  # value zajmuje 6 miejsc (z kropką), z czego 2 po przecinku
print(f"Wartość: {value: .2f}")
digit = 200
print(f"Wartość: {digit:4d}")
# ----------------------------
print("----------------------------")
print(f"A: {100:10d}")
print(f"B: {2500:10d}")
print(f"C: {100000000:10d}")
