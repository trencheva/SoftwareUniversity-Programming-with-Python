class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: list = []
        self.bill: float = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value.startswith('0') or len(value) != 10 or [el for el in value if not el.isdigit()]:
            raise ValueError("Invalid phone number!")

        self.__phone_number = value
