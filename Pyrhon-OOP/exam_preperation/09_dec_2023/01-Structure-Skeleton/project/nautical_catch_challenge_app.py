from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    def __init__(self):
        self.divers: list = []
        self.fish_list: list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):

        if diver_type not in ["FreeDiver", "ScubaDiver"]:
            return f"{diver_type} is not allowed in our competition."

        try:
            next(filter(lambda d: d.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."
        except StopIteration:
            self.divers.append(FreeDiver(diver_name) if diver_type == 'FreeDiver' else ScubaDiver(diver_name))
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in ["PredatoryFish", "DeepSeaFish"]:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            next(filter(lambda f: f.name == fish_name, self.fish_list))
            return f"{fish_name} is already permitted."
        except StopIteration:
            self.fish_list.append(PredatoryFish(fish_name, points) if fish_type == "PredatoryFish" else DeepSeaFish(fish_name, points))
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):

        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:

            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):

        unhealthy_divers_count = 0

        for diver in self.divers:
            if diver.has_health_issue:
                unhealthy_divers_count += 1

                diver.update_health_status()
                diver.renew_oxy()
        return f"Divers recovered: {unhealthy_divers_count}"

    def diver_catch_report(self, diver_name: str):
        result = f"**{diver_name} Catch Report**"
        diver = next(filter(lambda d: d.name == diver_name, self.divers))
        for fish in diver.catch:
            result += f"\n{fish.fish_details()}"

        return result

    def competition_statistics(self):
        result = "**Nautical Catch Challenge Statistics**"
        divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_divers = sorted(divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        for d in sorted_divers:
            result += f"\n{str(d)}"

        return result
