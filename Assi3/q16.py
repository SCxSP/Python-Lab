contacts = {}
for i in range(5):
    name = input("Enter name: ")
    contacts[name] = input("Enter phone: ")
s = input("Enter name to search: ")
print(contacts.get(s, "Not found"))
