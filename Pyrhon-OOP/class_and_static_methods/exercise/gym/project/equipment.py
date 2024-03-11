from project.get_next_id_mixin import GetNextIdMixin


class Equipment(GetNextIdMixin):
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.get_next_id()
        Equipment.increase_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

