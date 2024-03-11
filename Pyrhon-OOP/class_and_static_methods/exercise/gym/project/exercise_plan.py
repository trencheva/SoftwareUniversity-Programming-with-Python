from project.get_next_id_mixin import GetNextIdMixin


class ExercisePlan(GetNextIdMixin):

    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id()
        ExercisePlan.increase_id()

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
