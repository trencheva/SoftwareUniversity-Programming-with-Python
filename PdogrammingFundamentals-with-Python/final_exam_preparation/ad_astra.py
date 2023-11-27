import re

text = input()

pattern = r"(?i)([#|])([a-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"

matches = re.findall(pattern, text)
total_calories = sum([int(cal[3]) for cal in matches]) // 2000
print(f'You have food to last you for: {total_calories} days!')

for match in matches:
    product = match[1]
    date = match[2]
    calories = match[3]
    print(f'Item: {product}, Best before: {date}, Nutrition: {calories}')
