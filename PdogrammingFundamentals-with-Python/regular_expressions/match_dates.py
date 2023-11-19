import re

dates = input()

regex = r"([0-9]{2})([./-])([A-Z][a-z]{2})\2([0-9]{4})"

valid_dates = re.findall(regex, dates)

for date in valid_dates:
    print(f'Day: {date[0]}, Month: {date[2]}, Year: {date[3]}')