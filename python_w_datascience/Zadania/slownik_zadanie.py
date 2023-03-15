# Napisz funkcje o nazwie add_contacts, która przyjmie następujące argumenty:
#       - słownik z kontactami (dict)
#       - nazwę klucza (str)
#       - nr telefonu (str)
# Następnie funkcja wypisuje na konsoli komunikat:
#       - "Kontakt dodano", jeżeli dodaliśmy kontakt
#       - "Kontakt istnieje":, jeżeli podany klucz istnieje w słowniku
# Funkcja niczego nie zwraca (nie używamy return)

def add_contacts(contacts: dict, name: str, phone_nr: str) -> None:
    if name in contacts.keys():
        print("Kontakt istnieje")
    else:
        contacts[name] = phone_nr
        print("Kontakt dodano")


contact = {"Adam": "670234515", "Ewelina": "123456745", "Piotr": "000235423"}
imie = input("Prosze podać nazwę kontaktu: ")
numer = input("Prosze podać nr telefonu: ")
add_contacts(contact, imie, numer)
print(contact)
