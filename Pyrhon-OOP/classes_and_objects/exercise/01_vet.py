from typing import List


class Vet:

    animals: List[str] = []
    space: int = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name: str) -> str:

        if Vet.space > len(Vet.animals):
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"

        return "Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)

            return f"{animal_name} unregistered successfully"

        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space-len(Vet.animals)} space left in clinic"

