year = int(input())
while True:
    year += 1
    string_of_year = str(year)
    for index, digit in enumerate(string_of_year):
        if string_of_year.count(digit) > 1:
            break
    if string_of_year.count(digit) == 1:
        break
print(year)

# another option

# while True:
#     year += 1
#     year_as_string = str(year)
#     if len(year_as_string) == len(set(year_as_string)):
#         break
# print(year)
