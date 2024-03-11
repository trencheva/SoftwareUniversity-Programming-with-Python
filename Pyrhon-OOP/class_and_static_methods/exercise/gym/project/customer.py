from project.get_next_id_mixin import GetNextIdMixin


class Customer(GetNextIdMixin):
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()
        Customer.increase_id()

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"