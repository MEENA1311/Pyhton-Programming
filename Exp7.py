contacts = []
for _ in range(5):
    name = input("Enter name: ")
    number = input("Enter mobile number: ")
    contacts.append((name, number))

search_name = input("Enter the person name to search: ")
found = False
for contact in contacts:
    if contact[0].lower() == search_name.lower():
        print("Mobile Number is", contact[1])
        found = True
        break
if not found:
    print("Contact not found.")
