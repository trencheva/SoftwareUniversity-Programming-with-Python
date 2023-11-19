import re

number_of_lines = int(input())
pattern_name = r"@([A-Za-z]+)\|"
pattern_age = r"#(\d+)\*"

for line in range(number_of_lines):
    information = input()
    name_match = re.search(pattern_name, information)
    age_match = re.search(pattern_age, information)
    if name_match and age_match:
        print(f"{name_match.group(1)} is {age_match.group(1)} years old.")

