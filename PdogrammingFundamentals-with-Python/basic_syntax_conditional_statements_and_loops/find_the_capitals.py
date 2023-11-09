string = input()
result = []
for char in range(len(string)):
    if string[char].isupper():
        result.append(char)
print(result)