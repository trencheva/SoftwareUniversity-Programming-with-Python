def team_lineup(*players_info):
    countries_dict = {}
    result = []
    for player, country in players_info:
        countries_dict[country] = countries_dict.get(country, []) + [player]

    sorted_countries_dict = sorted(countries_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for country, players in sorted_countries_dict:
        result.append(f"{country}:")
        for player in players:
            result.append(f"-{player}")
    return '\n'.join(result)


print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))
