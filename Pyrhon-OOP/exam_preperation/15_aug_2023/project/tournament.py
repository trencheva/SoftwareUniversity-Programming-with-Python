from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    valid_equipments = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad,
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity: int = capacity
        self.equipment: list = []
        self.teams: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):

        if equipment_type not in self.valid_equipments:
            raise Exception("Invalid equipment type!")

        self.equipment.append(self.valid_equipments[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        valid_teams = {
            "OutdoorTeam": OutdoorTeam,
            "IndoorTeam": IndoorTeam,
        }

        if team_type not in valid_teams:
            raise Exception("Invalid team type!")

        if self.capacity <= len(self.teams):
            return "Not enough tournament capacity."

        self.teams.append(valid_teams[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):

        team = next(filter(lambda t: t.name == team_name, self.teams))

        if team.budget < self.valid_equipments[equipment_type].PRICE:
            raise Exception("Budget is not enough!")
        equipment = [el for el in self.equipment if type(el) == self.valid_equipments[equipment_type]][-1]
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        count = 0
        for eq in self.equipment:
            if type(eq) == self.valid_equipments[equipment_type]:
                eq.increase_price()
                count += 1
        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = [t for t in self.teams if t.name == team_name1][0]
        team2 = [t for t in self.teams if t.name == team_name2][0]

        if type(team1) != type(team2):
            raise Exception("Game cannot start! Team types mismatch!")

        team1_results = team1.advantage + sum(el.protection for el in team1.equipment)
        team2_results = team2.advantage + sum(el.protection for el in team2.equipment)

        if team1_results == team2_results:
            return "No winner in this game."
        elif team1_results > team2_results:
            team1.win()
            return f"The winner is {team1.name}."
        else:
            team2.win()
            return f"The winner is {team2.name}."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
        return f"Tournament: {self.name}\n" \
                 f"Number of Teams: {len(self.teams)}\n" \
                 f"Teams:\n" + '\n'.join(t.get_statistics() for t in sorted_teams)