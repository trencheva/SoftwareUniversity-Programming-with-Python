from project import Dough
from project import Topping


class Pizza:

    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: dict[Topping.topping_type: Topping.weight] = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")

        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")

        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")

        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping) -> str or None:
        # for t_type, t_weight in self.toppings.items():
            # if topping.topping_type == t_type:
            #     self.toppings[t_type] += topping.weight
            #     return
        if self.__max_number_of_toppings == len(self.toppings):
            raise ValueError("Not enough space for another topping")

        self.toppings[topping.topping_type] = self.toppings.get(topping.topping_type, 0) + topping.weight

    def calculate_total_weight(self):
        toppings_weight = sum(self.toppings.values())
        return toppings_weight + self.dough.weight
