class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f'Mammals in {self.name}: {", ".join(self.mammals)}'
        elif species == 'fish':
            result += f'Fishes in {self.name}: {", ".join(self.fishes)}'
        elif species == 'bird':
            result += f'Birds in {self.name}: {", ".join(self.birds)}'

        result += f'\nTotal animals: {self.__animals}'
        return result


name = input()
zoo_object = Zoo(name)

number_of_animals = int(input())

for current_animal in range(number_of_animals):
    species, name = input().split()

    zoo_object.add_animal(species, name)

species_info = input()
print(zoo_object.get_info(species_info))
