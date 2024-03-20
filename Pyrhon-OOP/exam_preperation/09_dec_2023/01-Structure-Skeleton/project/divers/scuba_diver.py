from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    INITIAL_OXYGEN_LEVEL = 540

    def __init__(self, name):
        super().__init__(name, ScubaDiver.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        try:
            self.oxygen_level -= round(time_to_catch * 0.30)
        except ValueError:
            self.oxygen_level = 0

        if self.oxygen_level == 0:
            self.update_health_status()

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.INITIAL_OXYGEN_LEVEL
