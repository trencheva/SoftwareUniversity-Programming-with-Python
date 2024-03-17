from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type, climber_name: str):
        if climber_type not in ["ArcticClimber", "SummitClimber"]:
            return f"{climber_type} doesn't exist in our register."

        if climber_name in [c.name for c in self.climbers]:
            return f"{climber_name} has been already registered."

        if climber_type == "ArcticClimber":
            self.climbers.append(ArcticClimber(climber_name))
        else:
            self.climbers.append(SummitClimber(climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type, peak_name: str, peak_elevation: int):

        if peak_type not in ["ArcticPeak", "SummitPeak"]:
            return f"{peak_type} is an unknown type of peak."

        if peak_type == "ArcticPeak":
            self.peaks.append(ArcticPeak(peak_name, peak_elevation))
        else:
            self.peaks.append(SummitPeak(peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear):

        peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        climber = [c for c in self.climbers if c.name == climber_name][0]

        missing_gear = []
        for el in peak.get_recommended_gear():
            if el not in gear:
                missing_gear.append(el)

        if missing_gear:
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. " \
                   f"Missing gear: {', '.join(sorted(missing_gear))}."

        return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.calculate_difficulty_level()}."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climbers = [c for c in self.climbers if c.conquered_peaks]
        conquered_peaks = []
        for c in climbers:
            conquered_peaks.extend(c.conquered_peaks)
        conquered_peaks_count = len(set(conquered_peaks))
        result = f"Total climbed peaks: {conquered_peaks_count}\n**Climber's statistics:**"

        sorted_climbers = sorted(climbers, key=lambda c: (-len(c.conquered_peaks), c.name))

        for c in sorted_climbers:
            result += f'\n{str(c)}'

        return result







