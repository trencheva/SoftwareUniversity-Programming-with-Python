phonebook = {}

while True:
    people_information = input()
    if "-" not in people_information:
        break

    name, phone_number = people_information.split('-')

    phonebook[name] = phone_number

searches = int(people_information)
for search in range(searches):
    name = input()
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
