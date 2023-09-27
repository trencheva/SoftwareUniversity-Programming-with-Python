animal_list = []
for lines in range(3):
    string = input()
    animal_list.append(string)
animal_list[0], animal_list[2] = animal_list[2], animal_list[0]
print(animal_list)