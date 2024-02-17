def forecast(*args):

    info_dict = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': [],
    }

    for destination, weather in args:
        info_dict[weather].append(destination)

    result = ''
    for weather, destinations in info_dict.items():
        if destinations:
            sorted_destinations = sorted(destinations)
            for destination in sorted_destinations:
                result += f"{destination} - {weather}\n"

    return result


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
