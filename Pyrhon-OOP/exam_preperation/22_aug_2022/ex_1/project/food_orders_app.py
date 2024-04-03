from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    PAID_BILL_NUMBER = 0
    VALID_MEALS = {
            "Starter": Starter,
            "MainDish": MainDish,
            "Dessert": Dessert}

    def __init__(self):
        self.menu: list = []
        self.clients_list: list = []

    def register_client(self, client_phone_number: str):
        try:
            next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
            raise Exception("The client has already been registered!")
        except StopIteration:
            self.clients_list.append(Client(client_phone_number))
            return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self) -> str:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return '\n'.join([meal.details() for meal in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        try:
            self.register_client(client_phone_number)
        except Exception:
            ...

        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        valid_meals = {}
        for name, quantity in meal_names_and_quantities.items():
            try:
                meal = next(filter(lambda m: m.name == name, self.menu))
                if meal.quantity < quantity:
                    raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {name}!")
                valid_meals[meal] = quantity
            except StopIteration:
                raise Exception(f"{name} is not on the menu!")

        for meal, quantity in valid_meals.items():
            client.shopping_cart.append(self.VALID_MEALS[meal.__class__.__name__](meal.name, meal.price, quantity))
            client.bill += quantity * meal.price
            menu_meal = next(filter(lambda m: m.name == name, self.menu))
            menu_meal.quantity -= quantity
        return f"Client {client_phone_number} successfully ordered {', '.join(m.name for m in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal_to_return in client.shopping_cart:
            meal = next(filter(lambda m: m.name == meal_to_return.name, self.menu))
            meal.quantity += meal_to_return.quantity

        client.shopping_cart = []
        client.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        FoodOrdersApp.PAID_BILL_NUMBER += 1
        total_paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0.0
        return f"Receipt #{FoodOrdersApp.PAID_BILL_NUMBER} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

