from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.hors_races = []

    def find_horse(self, horse_name):
        try:
            horse = next(filter(lambda h: h.name == horse_name, self.horses))
            return horse
        except StopIteration:
            return None

    def find_jockey(self, jockey_name):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
            return jockey
        except StopIteration:
            return None

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return
        if self.find_horse(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")
        self.horses.append(self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed))
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.find_jockey(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        try:
            next(filter(lambda r: r.race_type == race_type, self.hors_races))
            raise Exception(f"Race {race_type} has been already created!")
        except StopIteration:
            self.hors_races.append(HorseRace(race_type))
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_jockey(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken][-1]
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            horse_race = next(filter(lambda r: r.race_type == race_type, self.hors_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.find_jockey(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            horse_race = next(filter(lambda r: r.race_type == race_type, self.hors_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        the_fastest_jockey = sorted(horse_race.jockeys, key=lambda jockey: -jockey.horse.speed)[0]
        return f"The winner of the {race_type} race, with a speed of {the_fastest_jockey.horse.speed}km/h " \
               f"is {the_fastest_jockey.name}! Winner's horse: {the_fastest_jockey.horse.name}."







