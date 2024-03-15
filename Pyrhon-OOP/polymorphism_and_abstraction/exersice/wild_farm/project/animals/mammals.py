from project.food import Vegetable, Fruit, Meat
from project.animals.animal import Mammal


class Mouse(Mammal):

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def gained_weight(self):
        return 0.10

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]


class Cat(Mammal):

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def gained_weight(self):
        return 0.30

    @property
    def food_that_eats(self):
        return [Meat, Vegetable]


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def gained_weight(self):
        return 0.40

    @property
    def food_that_eats(self):
        return [Meat]


class Tiger(Mammal):

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def gained_weight(self):
        return 1.00

    @property
    def food_that_eats(self):
        return [Meat]

