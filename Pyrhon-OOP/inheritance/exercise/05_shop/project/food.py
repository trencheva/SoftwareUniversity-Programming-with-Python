from project import Product


class Food(Product):

    def __init__(self, name):
        super().__init__(name, quantity=15)

