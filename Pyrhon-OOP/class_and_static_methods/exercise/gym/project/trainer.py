from project.get_next_id_mixin import GetNextIdMixin


class Trainer(GetNextIdMixin):
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.get_next_id()
        Trainer.increase_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
