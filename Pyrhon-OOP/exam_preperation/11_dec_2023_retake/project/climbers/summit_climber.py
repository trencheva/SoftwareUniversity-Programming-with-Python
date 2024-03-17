from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    def __init__(self, name: str):
        super().__init__(name, strength=150)

    def can_climb(self) -> bool:
        return True if self.strength >= 75 else False

    def climb(self, peak: BasePeak):

        if peak.difficulty_level() == 'Extreme':
            self.strength -= 30 * 2.5
        else:
            self.strength -= 30 * 1.3

        self.conquered_peaks.append(peak.name)