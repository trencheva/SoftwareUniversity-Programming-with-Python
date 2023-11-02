input_line = input().split()
dictionary = {}

for element in input_line:
    if element.lower() in dictionary:
        dictionary[element.lower()] += 1
    else:
        dictionary[element.lower()] = 1


for k, count in dictionary.items():
    if count % 2 != 0:
        print(k, end=' ')
